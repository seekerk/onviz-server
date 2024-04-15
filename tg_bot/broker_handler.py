"""
Обработчик событий брокера сообщений для бота телеграма
"""
from tg_bot.tg_bot_handler import TgBotHandler


class BrokerHandler:
    """
    Обработчик событий брокера
    """

    # обработчик телеграм бота
    tg_handler: TgBotHandler = None

    def set_tg_handler(self, tg_handler):
        self.tg_handler = tg_handler
