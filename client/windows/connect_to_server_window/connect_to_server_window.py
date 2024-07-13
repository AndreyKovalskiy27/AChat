"""Модуль вікна підключення до сервера"""

from os import remove
from os.path import exists
from PyQt6.QtWidgets import QMainWindow, QFileDialog
from PyQt6.QtGui import QPixmap
from design.connect_to_server import ConnectToServerWindowDesign
from design import btn_locker
from windows.add_server_window import AddServerWindow
from connection.messages_monitor import MessagesMonitor
from connection.connection_thread import ConnectionThread
from connection.connection import Connection
from windows.connect_to_server_window.servers import (
    load_servers,
    apply_server,
    delete_server,
)
from windows.connect_to_server_window.connection_data import (
    load_connection_data,
    save_connection_data,
    check_not_empty,
)
import settings
import messages
import translation


class ConnectToServerWindow(QMainWindow):
    """Вікно підключення до сервера"""

    def __init__(self, main_window, language: str = "ua") -> None:
        super().__init__(main_window)

        self.design = ConnectToServerWindowDesign()
        self.design.setupUi(self, language)

        self.connection_data = settings.ConnectionData()
        self.servers = settings.Servers()
        self.language = settings.Language()
        self.avatar = settings.UserAvatar()

        self.main_window = main_window
        self.language_codes = {"Українська": "ua", "English": "en"}
        self.add_server_window = AddServerWindow(self, language)
        self.design.new_language.setCurrentText(
            dict(zip(self.language_codes.values(), self.language_codes.keys()))[
                self.language.get()
            ]
        )
        self.design.avatar.setPixmap(QPixmap(self.avatar.get_avatar_path()))
        load_connection_data(self)
        load_servers(self)

        # Натискання на кнопки
        self.design.connect_to_server.clicked.connect(self.connect_to_server)
        self.design.save.clicked.connect(lambda: save_connection_data(self))
        self.design.add_server.clicked.connect(self.add_server_window.show)
        self.design.delete_server.clicked.connect(lambda: delete_server(self))
        self.design.apply_server.clicked.connect(lambda: apply_server(self))
        self.design.set_language.clicked.connect(self.set_language)
        self.design.load_avatar.clicked.connect(self.set_avatar)
        self.design.delete_avatar.clicked.connect(self.delete_avatar)

    def connection_signal_handler(self, value) -> None:
        """Обробник сигналів з потока підключення до сервера"""
        if isinstance(value, Connection):
            self.main_window.connection = value
            self.main_window.messages_monitor = MessagesMonitor(
                self.main_window.connection, self.main_window
            )
            self.main_window.messages_monitor.start()

            self.close()
            btn_locker.lock_btn(self.design.connect_to_server)
            self.main_window.design.messages.clear()
            self.main_window.unblock_chat()
            self.main_window.add_message(
                translation.TRANSLATION[self.design.language]["connection_message"]
            )
            self.connection_thread.terminate()

        else:
            messages.show(
                translation.TRANSLATION[self.design.language][
                    "connection_to_server_error"
                ],
                translation.TRANSLATION[self.design.language][
                    "connection_to_server_error"
                ],
                messages.QMessageBox.Icon.Critical,
                value,
            )

    def connect_to_server(self) -> None:
        """Підключитися до серверу"""
        form_data = check_not_empty(self)

        if form_data:
            self.connection_thread = ConnectionThread(
                form_data[0], form_data[1], form_data[2]
            )
            self.connection_thread.signal.connect(self.connection_signal_handler)
            self.connection_thread.start()

    def set_language(self) -> None:
        """Встановити мову"""
        new_language = self.language_codes[self.design.new_language.currentText()]

        self.main_window.design.language = new_language
        self.design.language = new_language
        self.add_server_window.design.language = new_language

        self.main_window.design.retranslateUi(self.main_window, new_language)
        self.design.retranslateUi(self, new_language)
        self.add_server_window.design.retranslateUi(
            self.add_server_window, new_language
        )
        self.language.write(new_language)

    def set_avatar(self) -> None:
        """Встановити аватар"""
        new_avatar_file_path = QFileDialog.getOpenFileName(
            self, None, None, "Image (*.png *.jpg *.jpeg)"
        )[0]

        if new_avatar_file_path:
            self.avatar.set_avatar(new_avatar_file_path)
            self.design.avatar.setPixmap(QPixmap(new_avatar_file_path))

    def delete_avatar(self) -> None:
        """Видалити аватар"""
        if exists(self.avatar.user_avatar_file_path):
            remove(self.avatar.user_avatar_file_path)
            self.design.avatar.setPixmap(QPixmap(self.avatar.get_avatar_path()))
