"""Модуль для роботи з налаштуваннями программи"""


from typing import Union
from os.path import expanduser, join, exists
from os import mkdir, remove
from json import load, dump


class Settings:
    """Класс для роботи з налаштуваннями"""
    def __init__(self) -> None:
        self.settings_folder = join(expanduser("~"), ".achat-data")
        self.settings_file = join(self.settings_folder, "settings.json")

    def write(self, data: dict) -> None:
        """Записати данні у файл налаштуваннь"""
        if not exists(self.settings_folder):
            mkdir(self.settings_folder)

        if exists(self.settings_file):
            remove(self.settings_file)

        with open(self.settings_file, "w", encoding="utf-8") as settings_file:
            dump(data, settings_file, indent=4)

    def read(self) -> Union[dict, None]: 
        """Отримати данні з файла налаштуваннь"""
        try:
            with open(self.settings_file, "r") as settings_file:
                return load(settings_file)

        except:
            pass
