"""Модуль для роботи з налаштуваннями программи"""

from os.path import join, exists, getsize
from os import remove
from shutil import copy
from base64 import b64encode
from loguru import logger
from .settings_folder import SETTINGS_FOLDER


class AvatarTooHeavyError(Exception):
    """Ця помилка виникає коли користувач хоче встановити занадто великий аватар"""

class UserAvatar:
    """Класс для роботи з аватаром користувача"""

    def __init__(self) -> None:
        self.base_avatar_file_path = join("assets", "user.png")
        self.user_avatar_file_path = join(SETTINGS_FOLDER, "user.png")
        logger.success("Ініціалізовано класс для роботи з аватаром користувача")

    def has_own_avatar(self) -> bool:
        """Повертає True, якщо користувач встановив свій аватар. Інакше False"""
        if exists(self.user_avatar_file_path):
            return True

        return False

    def get_avatar_encoded(self) -> bytes:
        """Отримати аватар закодований через base64"""
        return b64encode(open(self.get_avatar_path(), "rb").read())

    def get_avatar_path(self) -> str:
        """Отримати шлях до аватару користувача"""
        if exists(self.user_avatar_file_path):
            return self.user_avatar_file_path

        return self.base_avatar_file_path

    def set_avatar(self, new_avatar_file_path: str) -> None:
        """Встановити аватар"""
        if exists(self.user_avatar_file_path):
            remove(self.user_avatar_file_path)

        size = getsize(new_avatar_file_path)

        if size > 94_491_520:
            raise AvatarTooHeavyError("Розмір аватара більше 90 мегабайт")

        copy(new_avatar_file_path, self.user_avatar_file_path)
        logger.success("Встановлений новий аватар")
