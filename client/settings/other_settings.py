"""Модуль для роботи з іншими налаштуванями программи"""

from typing import Union
from os.path import join, exists
from json import dump, load
from . import settings_folder


class OtherSettings:
    """Класс для роботи з іншими налаштуванями программи"""

    def __init__(self) -> None:
        self.other_settings_file_path = join(
            settings_folder.SETTINGS_FOLDER, "other.json"
        )

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

    def get_servers(self) -> Union[dict, None]:
        """Отримати список серверів"""
        if exists(self.other_settings_file_path):
            with open(
                self.other_settings_file_path, "r", encoding="utf-8"
            ) as other_settings_file:
                return load(other_settings_file)
