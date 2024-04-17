"""
Обработчик событий брокера сообщений для бота телеграма
"""
import asyncio
import json
import logging

from aiomqtt import MqttError, Client

from onviz_main.settings import BROKER_HOST, BROKER_PORT
from tg_bot.tg_bot_handler import TgBotHandler


class BrokerHandler:
    """
    Обработчик событий брокера
    """

    # обработчик телеграм бота
    tg_handler: TgBotHandler = None

    _is_stop = False

    def set_tg_handler(self, tg_handler):
        self.tg_handler = tg_handler

    async def start_subscription(self):
        """
        Запуск процесса подписки
        """
        reconnect_interval = 5  # In seconds
        while True:
            try:
                async with Client(BROKER_HOST, BROKER_PORT, identifier="tg_bot_" + str(id(self))) as client:
                    logging.debug("TG bot broker connected successfully")
                    await client.subscribe("service/#")
                    async for message in client.messages:
                        if self._is_stop:
                            break
                        topic = str(message.topic)
                        if topic == "service/ftp_server/upload_file":
                            self.tg_handler.notify_got_new_file(json.loads(message.payload))
            except MqttError as error:
                if self._is_stop:
                    return
                print(f'Error "{error}". Reconnecting in {reconnect_interval} seconds.')
                await asyncio.sleep(reconnect_interval)

    async def stop(self):
        self._is_stop = True
        await asyncio.sleep(1)