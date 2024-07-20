"""Модуль для роботи з іншими налаштуванями программи"""

from typing import Union
from os.path import join, exists
from json import dump, load
from loguru import logger
from . import settings_folder


class OtherSettings:
    """Класс для роботи з іншими налаштуванями программи"""

    def __init__(self) -> None:
        self.other_settings_file_path = join(
            settings_folder.SETTINGS_FOLDER, "other.json"
        )
        logger.success("Класс для роботи з іншими налаштуванями")

    def write(self, push_messages: bool, logging: bool, theme: str) -> None:
        """Записати данні у файл"""
        settings_folder.create_settings_folder()

        with open(
            self.other_settings_file_path, "w", encoding="utf-8"
        ) as other_settings_file:
            dump(
                {
                    "push_messages": push_messages,
                    "logging": logging,
                    "theme": theme,
                },
                other_settings_file,
                indent=4,
            )

        logger.success("Данні записані у JSON-файл")

    def get(self) -> Union[dict, None]:
        """Отримати інші налаштування"""
        if exists(self.other_settings_file_path):
            with open(
                self.other_settings_file_path, "r", encoding="utf-8"
            ) as other_settings_file:
                data = load(other_settings_file)
                logger.success("Данні отримані з JSON-файла")
                return data
