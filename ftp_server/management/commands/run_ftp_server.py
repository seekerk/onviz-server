"""
Команда запуска FTP сервера.
Сервер работает отдельным процессом параллельно серверу Django.
"""
import logging

from django.core.management import BaseCommand
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.servers import FTPServer

from ftp_server.ftp_server_handler import FtpServerHandler


class Command(BaseCommand):
    """
    Команда запуска FTP сервера.
    """

    def handle(self, *args, **options):
        """
        Запуск сервера
        """
        # TODO: переделать под пользователей Джанги
        authorizer = DummyAuthorizer()
        authorizer.add_user('user', '12345', homedir='.', perm='elradfmwMT')
        # authorizer.add_anonymous(homedir='.')

        handler = FtpServerHandler
        handler.authorizer = authorizer
        # TODO: брать параметры сервера из настроек
        server = FTPServer(('', 2121), handler)
        server.serve_forever()
