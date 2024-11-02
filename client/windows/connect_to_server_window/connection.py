"""Функції які відносяться до підключення до сервера"""

from loguru import logger
from connection.connection import Connection
from connection.connection_thread import ConnectionThread
from connection.messages_monitor import MessagesMonitor
from design.utils import btn_locker
from windows.main_window.add_message import add_message
from .connection_data import check_data
from design.utils import translation as translation
import messages


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
        add_message(
            self.main_window,
            translation.TRANSLATION[self.design.language]["connection_message"],
        )
        self.connection_thread.terminate()
        logger.success("Успішне підключення до сервер!")

    else:
        logger.error(f"Помилка під час підключення до сервера: {value}")
        messages.show(
            translation.TRANSLATION[self.design.language]["connection_to_server_error"],
            translation.TRANSLATION[self.design.language]["connection_to_server_error"],
            messages.QMessageBox.Icon.Critical,
            value,
        )


def connect_to_server(self) -> None:
    """Підключитися до серверу"""
    form_data = check_data(self)

    if form_data:
        self.connection_thread = ConnectionThread(
            form_data[0], form_data[1], form_data[2]
        )
        self.connection_thread.signal.connect(
            lambda value: connection_signal_handler(self, value)
        )
        self.connection_thread.start()
