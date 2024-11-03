"""Модуль вікна підключення до сервера"""

from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QPixmap
from loguru import logger
import design.add_server
import design.connect_to_server
import design.main_window
from windows.add_server_window import AddServerWindow
from .servers import (
    load_servers,
    apply_server,
    delete_server,
)
from .connection_data import (
    load_connection_data,
    save_connection_data,
)
from .connection import connect_to_server
from .avatar import set_avatar, delete_avatar
from .other_settings import load_other_settings, save_other_settings
import design
import settings


class ConnectToServerWindow(QMainWindow):
    """Вікно підключення до сервера"""

    def __init__(self, main_window, language: str = "ua") -> None:
        super().__init__(main_window)

        self.design = design.connect_to_server.ConnectToServerWindowDesign()
        self.design.setupUi(self, language)

        self.connection_data = settings.ConnectionData()
        self.servers = settings.Servers()
        self.language = settings.Language()
        self.avatar = settings.UserAvatar()
        self.other_settings = settings.OtherSettings()

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
        load_other_settings(self)

        self.setup_buttons()

        logger.success("Ініціалізовано вікно підключення до сервера")

    def setup_buttons(self):
        """Налаштувати обробники кнопок"""
        self.design.connect_to_server.clicked.connect(lambda: connect_to_server(self))
        self.design.save.clicked.connect(lambda: save_connection_data(self))
        self.design.add_server.clicked.connect(self.add_server_window.show)
        self.design.delete_server.clicked.connect(lambda: delete_server(self))
        self.design.apply_server.clicked.connect(lambda: apply_server(self))
        self.design.set_language.clicked.connect(self.set_language)
        self.design.load_avatar.clicked.connect(lambda: set_avatar(self))
        self.design.delete_avatar.clicked.connect(lambda: delete_avatar(self))
        self.design.save_other_settings.clicked.connect(
            lambda: save_other_settings(self)
        )

    def set_language(self) -> None:
        """Встановити мову"""
        logger.debug("set_language")
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
        logger.success(f"Мова встановлена: {new_language}")
