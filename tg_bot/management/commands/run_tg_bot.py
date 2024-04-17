"""
Команда запуска бота телеграм.
Бот работает отдельным процессом параллельно серверу Django.
"""
import asyncio
import logging

from django.core.management import BaseCommand
from telegram.ext import Application

from onviz_main.settings import TELEGRAM_BOT_TOKEN
from tg_bot.broker_handler import BrokerHandler
from tg_bot.tg_bot_handler import TgBotHandler

app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()


async def tg_adapter(tg_handler):
    """
    Запуск телеграм бота в asyncio
    """
    tg_handler.add_handlers(app)

    # see https://github.com/python-telegram-bot/python-telegram-bot/wiki/Frequently-requested-design-patterns#running-ptb-alongside-other-asyncio-frameworks
    await app.initialize()
    if app.post_init:
        await app.post_init()
    await app.start()
    await app.updater.start_polling()


async def _stop_tg():
    await app.updater.stop()
    await app.stop()
    await app.shutdown()
    return None


async def _stop_broker(handler):
    await handler.stop()


async def broker_adapter(broker_handler):
    await broker_handler.start_subscription()


def _handle_task_result(task: asyncio.Task):
    """
    Обработка завершения задачи
    :param task: задача
    """
    try:
        task.result()
    except asyncio.CancelledError:
        pass
    except Exception:
        logging.exception('Task failed: %r', task)
        task.get_loop().stop()


def _handle_tg_task_result(task: asyncio.Task):
    try:
        task.result()
    except asyncio.CancelledError:
        pass
    except Exception:
        logging.exception('Task failed: %r', task)
        task.get_loop().stop()


class Command(BaseCommand):
    """
    Команда запуска бота телеграм
    """

    def handle(self, *args, **options):
        """
        Запуск адаптеров для бота и брокера
        """

        tg_handler = TgBotHandler()
        broker_handler = BrokerHandler()
        tg_handler.set_broker_handler(broker_handler)
        broker_handler.set_tg_handler(tg_handler)

        loop = asyncio.get_event_loop()
        task = loop.create_task(tg_adapter(tg_handler))
        task.add_done_callback(_handle_tg_task_result)
        task = loop.create_task(broker_adapter(broker_handler))
        task.add_done_callback(_handle_task_result)

        try:
            loop.run_forever()
        except KeyboardInterrupt:
            task = loop.create_task(_stop_tg())
            loop.run_until_complete(asyncio.gather(task))
            task = loop.create_task(_stop_broker(broker_handler))
            loop.run_until_complete(asyncio.gather(task))
            loop.close()
            return
