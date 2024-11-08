"""Модуль для роботи з списком серверів"""

from typing import Union
from os.path import join, exists
from json import dump, load
from loguru import logger
from . import settings_folder


class Servers:
    """Класс для роботи з серверами"""

    def __init__(self) -> None:
        self.servers_file_path = join(settings_folder.SETTINGS_FOLDER, "servers.json")
        logger.success("Ініціалізовано класс для роботи з списком серверів")

    def write(self, data: dict) -> None:
        """Записати данні у файл серверів"""
        settings_folder.create_settings_folder()

        with open(self.servers_file_path, "w", encoding="utf-8") as servers_file:
            dump(data, servers_file, indent=4)

        logger.success("Данні записані у JSON-файл")

    def add_server(self, name: str, ip: str, port: int) -> None:
        """Додати сервер"""
        servers = self.get_servers()

        if name in servers.keys():
            raise ValueError("Server exists")

        servers[name] = {"ip": ip, "port": port}
        self.write(servers)
        logger.success("Сервер доданий")

    def delete_server(self, name: str) -> None:
        """Видалити сервер"""
        servers = self.get_servers()
        servers.pop(name)
        self.write(servers)
        logger.success("Сервер видалений")

    def get_servers(self) -> Union[dict, None]:
        """Отримати список серверів"""
        if exists(self.servers_file_path):
            with open(self.servers_file_path, "r", encoding="utf-8") as servers_file:
                data = load(servers_file)
                logger.success("Данні отримані з JSON-файла")
                return data

        return {}
