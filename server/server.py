"""Сервер"""


from typing import Any
from threading import Thread
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
        self.users = {}

        print("Сервер запущений!")
        self.connections_handler()

    def connections_handler(self) -> None:
        """Обробник підключеннь"""
        while True:
            try:
                user = self.server_socket.accept()[0]
                user.send(chiper.dumps(self.chiper.key_str))

                data = user.recv(1024)
                data = self.chiper.decrypt(data)

                if data["type"] == "client_ok":
                    nikname = data["nikname"]

                    if nikname in self.users.values():
                        self.send_to_user({"type": "server_not_ok", "message": "Такий нікнейм вже зайнятий"},
                                          user)

                    else:
                        self.users[user] = nikname

                        Thread(target=self.user_handler,
                            args=(user, nikname)).start()

                        self.send_to_user({"type": "server_ok", "message": "Ви успішно підключенні до сервера"}, user)
                        print(f"{nikname} приєднався до чату")

            except Exception: 
                pass

    def user_handler(self, user_socket: socket.socket, nikname: str) -> None:
        """Обробник користувача"""
        while True:
            try:
                data = user_socket.recv(1024)
                data = self.chiper.decrypt(data)

                # Запрос на відправку повідомлення
                if data["type"] == "message":
                    message: str = data["message"]

                    if not message.strip():
                        self.send_to_user({"type": "server_not_ok", "message": "Повідомлення не може бути пустим"}, user_socket)

                    else:
                        self.send_to_all(
                            {"type": "message",
                            "message": message,
                            "nikname": nikname},
                            user_socket
                        )
                        self.send_to_user({"type": "server_ok", "message": "Повідомлення було успішно відправленно"}, user_socket)
                        print(f"{nikname}: {message}")

                # Запрос на відключення
                elif data["type"] == "exit":
                    self.users.pop(user_socket)
                    self.send_to_all({"type": "exit", "nikname": nikname})
                    self.send_to_user({"type": "server_ok", "message": "Ви успішно були відʼєднані від сервера"}, user_socket)
                    user_socket.close()
                    print(f"{nikname} вийшов")
                    break

            except:
                try:
                    self.users.pop(user_socket)

                except:
                    pass

                print(f"{nikname} був видалений з сервера через помилку")

    def send_to_user(self, message: Any, user: socket.socket) -> None:
        """Відправити повідомлення конкретному користувачу"""
        message = self.chiper.encrypt(message)
        user.send(message)

    def send_to_all(self, message: Any,
                    do_not_send_to: socket.socket=None) -> None:
        """Відправити повідомлення всім користувачам на сервері"""
        for user in self.users.values():
            if user != do_not_send_to:
                try:
                    self.send_to_user(message, user)

                except:
                    try:
                        self.users.pop(user)

                    except:
                        pass