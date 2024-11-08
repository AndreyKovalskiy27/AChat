"""Модуль для роботи з данними для підключення до серверу"""

from typing import Union
from os.path import join, exists
from os import remove
from json import load, dump
from loguru import logger
from . import settings_folder


class ConnectionData:
    """Класс для роботи з данними для підключення до серверу"""

    def __init__(self) -> None:
        self.connection_data_file_path = join(
            settings_folder.SETTINGS_FOLDER, "connection_data.json"
        )
        logger.success(
            "Ініціалізован класс для роботи з данними для підключення до серверу"
        )

    def write(self, ip: str, port: int, nikname: str) -> None:
        """Записати IP, порт та нікнейм у файл"""
        settings_folder.create_settings_folder()

        if exists(self.connection_data_file_path):
            remove(self.connection_data_file_path)

        with open(
            self.connection_data_file_path, "w", encoding="utf-8"
        ) as connection_data_file:
            dump(
                {"ip": ip, "port": port, "nikname": nikname},
                connection_data_file,
                indent=4,
            )

        logger.success("Данні записані у JSON-файл")

    def read(self) -> Union[dict, None]:
        """Отримати данні з файла"""
        try:
            with open(self.connection_data_file_path, "r") as connection_data_file:
                data = load(connection_data_file)
                logger.success("Данні отримані з JSON-файла")
                return data

        except Exception:
            pass
