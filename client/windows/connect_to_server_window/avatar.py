"""Функції які відносяться до роботи з аватаром користувача"""

from os import remove
from os.path import exists
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtGui import QPixmap
from loguru import logger


def set_avatar(self) -> None:
    """Встановити аватар"""
    new_avatar_file_path = QFileDialog.getOpenFileName(
        self, None, None, "Image (*.png *.jpg *.jpeg)"
    )[0]

    if new_avatar_file_path:
        self.avatar.set_avatar(new_avatar_file_path)
        self.design.avatar.setPixmap(QPixmap(new_avatar_file_path))
        logger.success("Встановлений новий аватар користувача")


def delete_avatar(self) -> None:
    """Видалити аватар"""
    if exists(self.avatar.user_avatar_file_path):
        remove(self.avatar.user_avatar_file_path)
        self.design.avatar.setPixmap(QPixmap(self.avatar.get_avatar_path()))
        logger.success("Аватар користувача видалений")
