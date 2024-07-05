"""Сервер"""


import socket
import chiper


class Server:
    """Сервер"""
    def __init__(self, ip: str, port: int, max_users: int=0) -> None:
        self.server_socket = socket.socket(socket.AF_INET,
                                           socket.SOCK_STREAM)
        self.server_socket.bind((ip, port))
        self.server_socket.listen(max_users)
        self.chiper = chiper.Chiper()

        print("Сервер запущений!")

        self.connections_handler()

    def connections_handler(self) -> None:
        """Обробник підключеннь"""
        while True:
            try:
                user, adress = self.server_socket.accept()
                user.send(chiper.dumps(self.chiper.key_str))

                data = user.recv(1024)
                data = self.chiper.decrypt(data)

                if data["type"] == "client_ok":
                    user.send(self.chiper.encrypt("Hello world!"))

            except Exception: 
                pass

    def user_handler(self) -> None:
        """Обробник користувача"""
        ...
