"""Модуль для роботи з налаштуваннями программи"""


from typing import Union
from os.path import expanduser, join, exists
from os import mkdir, remove
from json import load, dump


SETTINGS_FOLDER = join(expanduser("~"), ".achat-data")


class ConnectionData:
    """Класс для роботи з данними для підключення до серверу"""
    def __init__(self) -> None:
        self.connection_data_file_path = join(SETTINGS_FOLDER, "settings.json")

    def write(self, ip: str, port: int, nikname: str) -> None:
        """Записати данні у файл"""
        if not exists(SETTINGS_FOLDER):
            mkdir(SETTINGS_FOLDER)

        if exists(self.connection_data_file_path):
            remove(self.connection_data_file_path)

        with open(self.connection_data_file_path, "w", encoding="utf-8") as connection_data_file:
            dump({"ip": ip, "port": port, "nikname": nikname}, connection_data_file, indent=4)

    def read(self) -> Union[dict, None]: 
        """Отримати данні з файла"""
        try:
            with open(self.connection_data_file_path, "r") as connection_data_file:
                return load(connection_data_file)

        except:
            pass
