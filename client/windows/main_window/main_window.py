"""Модуль головного вікна"""

from os.path import join
from PyQt6.QtWidgets import QMainWindow, QSystemTrayIcon, QMenu
from PyQt6.QtGui import QIcon, QAction, QShortcut, QKeySequence
from PyQt6.QtCore import QSize
from loguru import logger
from design import main_window
from design.utils import btn_locker
from windows.connect_to_server_window import ConnectToServerWindow
from settings import Language
from . import connection, select_sticker


class MainWindow(QMainWindow):
    """Головне вікно"""

    def __init__(self) -> None:
        super().__init__()

        language = Language().get()
        self.is_connected = False

        self.design = main_window.MainWindowDesign()
        self.design.setupUi(self, language)
        self.design.messages.setIconSize(QSize(70, 70))
        self.block_chat()

        self.connect_to_server_window = ConnectToServerWindow(self, language)

        # Меню программи у панелі управління
        self.tray_icon = QSystemTrayIcon(QIcon(join("assets", "icon.png")), self)

        menu = QMenu()
        connect_to_server_action = QAction("Підключитися до серверу", self)
        connect_to_server_action.triggered.connect(self.connect_to_server_window.show)
        exit_server_action = QAction("Вийти з серверу", self)
        exit_server_action.triggered.connect(lambda: connection.exit_from_server(self))
        quit_achat_action = QAction("Закрити AChat", self)
        quit_achat_action.triggered.connect(
            lambda: (connection.exit_from_server(self), exit(0))
        )
        menu.addAction(connect_to_server_action)
        menu.addAction(exit_server_action)
        menu.addAction(quit_achat_action)
        self.tray_icon.setContextMenu(menu)
        self.tray_icon.show()

        self.setup_buttons()
        logger.success("Ініціалізоване головне вікно")

    def setup_buttons(self):
        """Налаштувати обробники кнопок"""
        select_sticker.setup_stickers(self)
        self.design.connect_to_server.clicked.connect(
            self.connect_to_server_window.show
        )
        self.design.send_message.clicked.connect(lambda: connection.send_message(self))
        QShortcut(QKeySequence("Return"), self).activated.connect(
            lambda: connection.send_message(self)
        )  # Відправка повідомлення по Enter
        self.design.exit.clicked.connect(lambda: connection.exit_from_server(self))

    def block_chat(self) -> None:
        """Заблокувати чат (кнопки для відправки повідомлення та виходу з сервера)"""
        btn_locker.lock_btn(self.design.send_message)
        btn_locker.lock_btn(self.design.exit)
        logger.success("Чат заблокований")

    def unblock_chat(self) -> None:
        """Розблокувати чат (кнопки для відправки повідомлення та виходу з сервера)"""
        btn_locker.unlock_btn(self.design.send_message)
        btn_locker.unlock_btn(self.design.exit)
        logger.success("Чат розблокований")

    def closeEvent(self, a0) -> None:
        """
        Цей код виконується під час виходу з программи
        В данному випадку виконується автоматичний вихід з серверу
        """
        connection.exit_from_server(self)
        a0.accept()
