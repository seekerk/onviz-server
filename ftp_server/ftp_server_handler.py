"""
Обработчик подключений к FTP серверу
"""

from aiomqtt import Client
from pyftpdlib.handlers import FTPHandler


async def send_message(topic, message):
    async with Client("localhost", 1883) as client:
        await client.publish(topic, str(message))


class FtpServerHandler(FTPHandler):
    """
    Обработчик подключений к FTP серверу
    """
    loop: None

    def on_connect(self):
        """
        Подключение пользователя, уведомляем всех
        """
        print("%s:%s connected" % (self.remote_ip, self.remote_port))
        coro = send_message(topic="service/ftp_server/connected",
                            message={"host": self.remote_ip, "port": self.remote_port})
        self.loop.run_until_complete(coro)

    def on_disconnect(self):
        # do something when client disconnects
        pass

    def on_login(self, username):
        # do something when user login
        pass

    def on_logout(self, username):
        # do something when user logs out
        pass

    def on_file_sent(self, file):
        # do something when a file has been sent
        pass

    def on_file_received(self, file):
        # do something when a file has been received
        pass

    def on_incomplete_file_sent(self, file):
        # do something when a file is partially sent
        pass

    def on_incomplete_file_received(self, file):
        # remove partially uploaded files
        import os
        os.remove(file)
