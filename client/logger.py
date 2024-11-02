"""Модуль для увімкнення та вимкнення логування"""

from sys import stdout
from os.path import join, expanduser
from settings.settings_folder import SETTINGS_FOLDER
from datetime import datetime
from loguru import logger


def disable() -> None:
    """Вимкнути логування"""
    logger.remove()
    logger.add(stdout, level="DEBUG")


def enable() -> None:
    """Увімкнути логування"""
    logger.add(
        join(
            expanduser("~"),
            SETTINGS_FOLDER,
            "logs",
            datetime.now().strftime("%Y-%m-%d %H-%M-%S"),
        ),
        level="DEBUG",
    )
