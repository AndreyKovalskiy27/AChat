"""Сервер"""

from typing import Any
from threading import Thread
import socket
import chiper
import rsa


class Server:
    """Сервер"""

    def __init__(self, ip: str, port: int, max_users: int = 0) -> None:
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((ip, port))
        self.server_socket.listen(max_users)

        self.users = {}

        print("Сервер запущений!")
        self.connections_handler()

    def connections_handler(self) -> None:
        """Обробник підключеннь"""
        while True:
            try:
                user = self.server_socket.accept()[0]

                # Відправка клієнту ключа шифрування
                user_public_key = user.recv(100000)
                user_public_key = rsa.PublicKey.load_pkcs1(user_public_key)
                user_chiper = chiper.Chiper()
                user.send(rsa.encrypt(user_chiper.key_str, user_public_key))

                data = user.recv(100000)
                data = user_chiper.decrypt(data)

                if data["type"] == "client_ok":
                    nikname = data["nikname"]
                    is_nikname_avalible = True

                    # Перевірка на те, що нікнейм не зайнятий
                    for value in self.users.values():
                        if value["nikname"] == nikname:
                            is_nikname_avalible = False
                            user.send(
                                user_chiper.encrypt(
                                    {
                                        "type": "server_not_ok",
                                        "message": "This nikname is already taken",
                                    },
                                )
                            )

                    if is_nikname_avalible:
                        self.send_to_all({"type": "new_user", "nikname": nikname})
                        self.users[user] = {"nikname": nikname, "chiper": user_chiper}

                        Thread(target=self.user_handler, args=(user,)).start()

                        self.send_to_user(
                            {
                                "type": "server_ok",
                                "message": "Ви успішно підключенні до сервера",
                            },
                            user,
                        )
                        print(f"{nikname} приєднався до чату")

            except Exception:
                pass

    def user_handler(self, user_socket: socket.socket) -> None:
        """Обробник користувача"""
        nikname = self.users[user_socket]["nikname"]

        while True:
            try:
                data = user_socket.recv(100000)
                data = self.users[user_socket]["chiper"].decrypt(data)

                # Запрос на відправку повідомлення
                if data["type"] == "message":
                    message: str = data["message"]

                    if message.strip():
                        self.send_to_all(
                            {
                                "type": "message",
                                "message": message,
                                "nikname": nikname,
                                "avatar": data.get("avatar", None),
                            },
                            user_socket,
                        )
                        print(f"{nikname}: {message}")

                # Запрос на відключення
                elif data["type"] == "exit":
                    self.users.pop(user_socket)
                    self.send_to_all({"type": "exit", "nikname": nikname})
                    user_socket.close()
                    print(f"{nikname} вийшов")
                    break

            except Exception:
                try:
                    self.users.pop(user_socket)

                except Exception:
                    pass

                self.send_to_all({"type": "exit", "nikname": nikname})
                print(f"{nikname} був видалений з сервера через помилку")
                break

    def send_to_user(self, message: Any, user: socket.socket) -> None:
        """Відправити повідомлення конкретному користувачу"""
        message = self.users[user]["chiper"].encrypt(message)
        user.sendall(message)

    def send_to_all(self, message: Any, do_not_send_to: socket.socket = None) -> None:
        """Відправити повідомлення всім користувачам на сервері"""
        for user in self.users.keys():
            if user != do_not_send_to:
                try:
                    self.send_to_user(message, user)

                except Exception:
                    try:
                        self.users.pop(user)
                        print(
                            f"{self.users[user]} був видалений з сервера через помилку"
                        )

                    except Exception:
                        pass
