"""
Обработчик событий телеграма
"""
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext


class TgBotHandler:
    """
    Обработчик событий телеграма
    """

    # обработчик событий пользователя (BrokerHandler)
    broker_handler = None

    def set_broker_handler(self, broker_handler):
        self.broker_handler = broker_handler

    def add_handlers(self, app):
        """
        Подключение обработчиков команд телеграма
        :param app:
        """
        app.add_handler(CommandHandler("start", self.start))

    @staticmethod
    async def start(update: Update, context: CallbackContext):
        """
        Регистрация пользователя бота
        :param update:
        :param context:
        :return:
        """
        print(context.args)

    def notify_got_new_file(self, param):
        """
        Сообщение пользователю бота о появлении нового файла
        :param param: параметры файла
        """
        print(param)
