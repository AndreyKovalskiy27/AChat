"""Модуль для зʼєднання з сервером"""


from typing import Any
import socket
from connection import chiper


class Connection:
    """Класс для зʼєднання з сервером"""
    def __init__(self, ip: str, port: int, nikname: str) -> None:
        self.nikname = nikname

        self.connection_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection_socket.connect((ip, port))
        self.connection_socket.settimeout(3)

        key_str = chiper.loads(self.connection_socket.recv(1024))

        self.chiper = chiper.Chiper(key_str)
        self.send_message({"type": "client_ok", "nikname": nikname})

        server_answer: dict = self.get_data_from_server()

        if server_answer["type"] != "server_ok":
            raise ConnectionError(server_answer.get("message",
                                                    "The server did not give you permission to connect"))

    def get_data_from_server(self) -> Any:
        """Отримати данні з серверу"""
        self.connection_socket.settimeout(1)
        data = self.connection_socket.recv(1024)
        data = self.chiper.decrypt(data)
        self.connection_socket.settimeout(None)
        return data

    def send_message(self, message: Any) -> None:
        """Відправити повідомлення на сервер"""
        self.connection_socket.send(self.chiper.encrypt(message))

    def exit(self) -> None:
        """Вийти з серверу"""
        self.send_message({"type": "exit"})
        self.connection_socket.close()
