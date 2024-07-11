"""Модуль для роботи з налаштуваннями программи"""


from typing import Union
from os.path import expanduser, join, exists
from os import mkdir, remove
from json import load, dump


SETTINGS_FOLDER = join(expanduser("~"), ".achat-data")

def create_settings_folder() -> None:
    """Створити папку налаштуваннь"""
    if not exists(SETTINGS_FOLDER):
        mkdir(SETTINGS_FOLDER)


class ConnectionData:
    """Класс для роботи з данними для підключення до серверу"""
    def __init__(self) -> None:
        self.connection_data_file_path = join(SETTINGS_FOLDER, "connection_data.json")

    def write(self, ip: str, port: int, nikname: str) -> None:
        """Записати IP, порт та нікнейм у файл"""
        create_settings_folder()

        if exists(self.connection_data_file_path):
            remove(self.connection_data_file_path)

        with open(self.connection_data_file_path, "w", encoding="utf-8") as connection_data_file:
            dump({"ip": ip, "port": port, "nikname": nikname},
                 connection_data_file, indent=4)

    def read(self) -> Union[dict, None]: 
        """Отримати данні з файла"""
        try:
            with open(self.connection_data_file_path, "r") as connection_data_file:
                return load(connection_data_file)

        except Exception:
            pass


class Servers:
    """Класс для роботи з серверами"""
    def __init__(self) -> None:
        self.servers_file_path = join(SETTINGS_FOLDER, "servers.json")

    def write(self, data: dict) -> None:
        """Записати данні у файл серверів"""
        create_settings_folder()

        with open(self.servers_file_path, "w", encoding="utf-8") as servers_file:
            dump(data, servers_file, indent=4)

    def add_server(self, name: str, ip: str, port: int) -> None:
        """Додати сервер"""
        servers = self.get_servers()

        if name in servers.keys():
            raise ValueError("Server exists")

        servers[name] = {"ip": ip, "port": port}
        self.write(servers)

    def delete_server(self, name: str) -> None:
        """Видалити сервер"""
        servers = self.get_servers()
        servers.pop(name)
        self.write(servers)

    def get_servers(self) -> Union[dict, None]:
        """Отримати список серверів"""
        if exists(self.servers_file_path):
            with open(self.servers_file_path, "r", encoding="utf-8") as servers_file:
                return load(servers_file)

        return {}
