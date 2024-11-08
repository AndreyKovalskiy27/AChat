"""Папка, де зберігаються налаштування"""

from os.path import join, expanduser, exists
from os import mkdir
from loguru import logger


SETTINGS_FOLDER = join(expanduser("~"), ".achat-data")


def create_settings_folder() -> None:
    """Створити папку налаштуваннь"""
    if not exists(SETTINGS_FOLDER):
        mkdir(SETTINGS_FOLDER)
        logger.success("Створенно папку налаштуваннь")
