"""Моніторинг повідомленнь від сервера"""

from os.path import join, exists
from base64 import b64decode
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt, QThread
from connection.connection import Connection
from . import users_handler
from .message_handler import message_handler
import translation


class MessagesMonitor(QThread):
    """Монітогинг повідомленнь від сервера та вивід на єкран"""

    def __init__(self, connection: Connection, main_window) -> None:
        super().__init__()
        self.connection = connection
        self.main_window = main_window

    def run(self) -> None:
        """Запустити монітогинг повідомленнь від сервера та вивід на єкран"""
        self.connection.connection_socket.settimeout(None)

        while True:
            try:
                data = self.connection.get_data_from_server()

                if data["type"] == "message":
                    message_handler(data, self.main_window)

                elif data["type"] == "new_user":
                    users_handler.user_connection_handler(data, self.main_window)

                elif data["type"] == "exit":
                    users_handler.user_exit_handler(data, self.main_window)

            except Exception:
                pass
