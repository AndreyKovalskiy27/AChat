"""Модуль для роботи з мовою программи"""

from json import dump, load
from os.path import join, exists
from os import remove
from loguru import logger
from . import settings_folder


class Language:
    """Класс для роботи з мовою программи"""

    def __init__(self) -> None:
        self.language_file_path = join(settings_folder.SETTINGS_FOLDER, "language.json")
        logger.success("Ініціалізовано класс для роботи з мовою программи")

    def write(self, language: str) -> None:
        """Записати мову у файл"""
        settings_folder.create_settings_folder()

        if exists(self.language_file_path):
            remove(self.language_file_path)

        with open(self.language_file_path, "w", encoding="utf-8") as language_file:
            dump({"language": language}, language_file, indent=4)

        logger.success("Данні записані у JSON-файл")

    def get(self) -> str:
        """Отримати мову"""
        if exists(self.language_file_path):
            try:
                with open(self.language_file_path, "r") as language_file:
                    data = load(language_file)["language"]
                    logger.success("Данні отримані з JSON-файла")
                    return data

            except Exception:
                return "ua"

        return "ua"
