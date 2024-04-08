"""
Команда запуска бота телеграм.
Бот работает отдельным процессом параллельно серверу Django.
"""
import logging

from django.core.management import BaseCommand


class Command(BaseCommand):
    """
    Команда запуска бота телеграм
    """

    def handle(self, *args, **options):
        """
        Запуск бота
        """
        logging.debug("Запуск телеграм бота")
