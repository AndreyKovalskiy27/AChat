"""Обробка кнопок для роботи з серверами"""

from os import remove
from PyQt6.QtWidgets import QTableWidgetItem
from loguru import logger
import messages
from design.utils import translation as translation


def load_servers(self) -> None:
    """Завантажити сервери"""
    try:
        servers = self.servers.get_servers()
        self.design.servers.setRowCount(len(servers.keys()))
        row = 0

        for server in servers.keys():
            self.design.servers.setItem(row, 0, QTableWidgetItem(server))
            self.design.servers.setItem(row, 1, QTableWidgetItem(servers[server]["ip"]))
            self.design.servers.setItem(
                row, 2, QTableWidgetItem(str(servers[server]["port"]))
            )
            row += 1

        logger.success("Завантаженний список серверів")

    except Exception as error:
        logger.error(f"Помилка під час завантаження списку серверів: {error}")
        remove(self.servers.servers_file_path)


def apply_server(self) -> None:
    """Встановити IP та порт вибранного сервера"""
    row = self.design.servers.currentRow()

    if row > -1:
        self.design.ip.setText(self.design.servers.item(row, 1).text())
        self.design.port.setText(self.design.servers.item(row, 2).text())
        logger.success("IP та порт вибранного сервера встановлені")


def delete_server(self) -> None:
    """Видалити сервер"""
    row = self.design.servers.currentRow()

    if row > -1:
        try:
            server_name = self.design.servers.item(row, 0).text()
            self.servers.delete_server(server_name)
            load_servers(self)
            logger.success("Сервер видаленний")

        except Exception as error:
            logger.error(f"Помилка під час видалення серверу: {error}")
            load_servers(self)
            messages.show(
                translation.TRANSLATION[self.design.language]["server_deletion_error"],
                translation.TRANSLATION[self.design.language]["server_deletion_error"],
                messages.QMessageBox.Icon.Critical,
                error,
            )
