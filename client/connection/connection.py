"""Модуль для зʼєднання з сервером"""

from typing import Any
import socket
from connection import chiper
from loguru import logger
import rsa


class Connection:
    """Класс для зʼєднання з сервером"""

    def __init__(self, ip: str, port: int, nikname: str) -> None:
        self.nikname = nikname

        self.connection_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection_socket.connect((ip, port))
        self.connection_socket.settimeout(3)
        logger.success("Створенне підключення з сервером")

        # Отримання ключа шифрування від сервера
        public_key, private_key = rsa.newkeys(500)
        self.connection_socket.send(public_key.save_pkcs1())
        key_str = self.connection_socket.recv(100000)
        key_str = rsa.decrypt(key_str, private_key)
        logger.success("Отриманий ключ шифрування від сервера")

        self.chiper = chiper.Chiper(key_str)
        self.send_message({"type": "client_ok", "nikname": nikname})

        server_answer: dict = self.get_data_from_server()

        if server_answer["type"] != "server_ok":
            raise ConnectionError(
                server_answer.get(
                    "message", "The server did not give you permission to connect"
                )
            )

        logger.success("Успішне підключення до серверу")

    def get_data_from_server(self) -> Any:
        """Отримати данні з серверу"""
        data = self.connection_socket.recv(100000)
        data = self.chiper.decrypt(data)
        logger.debug("Отриманні данні з серверу: ######")
        return data

    def send_message(self, message: Any) -> None:
        """Відправити повідомлення на сервер"""
        self.connection_socket.sendall(self.chiper.encrypt(message))
        logger.success("Відправлено повідомлення до серверу")
