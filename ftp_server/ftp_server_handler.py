"""
Обработчик подключений к FTP серверу
"""
import json

from aiomqtt import Client, MqttError
from pyftpdlib.handlers import FTPHandler

from onviz_main.settings import BROKER_HOST, BROKER_PORT


async def send_message(topic, message):
    try:
        async with Client(BROKER_HOST, BROKER_PORT) as client:
            await client.publish(topic, json.dumps(message))
    except MqttError as e:
        print(e, topic, message)


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
        coro = send_message(topic="service/ftp_server/login",
                            message={"username": username})
        self.loop.run_until_complete(coro)

    def on_logout(self, username):
        # do something when user logs out
        pass

    def on_file_sent(self, file):
        # do something when a file has been sent
        pass

    def on_file_received(self, file):
        # do something when a file has been received
        coro = send_message(topic="service/ftp_server/upload_file",
                            message={"file": file, "user": self.username})
        self.loop.run_until_complete(coro)

    def on_incomplete_file_sent(self, file):
        # do something when a file is partially sent
        pass

    def on_incomplete_file_received(self, file):
        # remove partially uploaded files
        import os
        os.remove(file)
