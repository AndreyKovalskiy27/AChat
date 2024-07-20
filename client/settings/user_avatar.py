"""Модуль для роботи з налаштуваннями программи"""

from os.path import join, exists
from os import remove
from shutil import copy
from base64 import b64encode
from .settings_folder import SETTINGS_FOLDER


class UserAvatar:
    """Класс для роботи з аватаром користувача"""

    def __init__(self) -> None:
        self.base_avatar_file_path = join("assets", "user.png")
        self.user_avatar_file_path = join(SETTINGS_FOLDER, "user.png")

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

        copy(new_avatar_file_path, self.user_avatar_file_path)
