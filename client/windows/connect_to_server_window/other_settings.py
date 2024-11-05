"""Модуль для роботи з іншими налаштуваннями"""

from os import remove
from loguru import logger
from logger import enable, disable
from design.themes.css import dark, light


def load_other_settings(self) -> None:
    """Завантажити інші налаштування"""
    try:
        other_settings = self.other_settings.get()

        if other_settings:
            self.design.push_messages.setChecked(other_settings["push_messages"])
            self.design.logging.setChecked(other_settings["logging"])
            self.design.new_theme.setCurrentIndex(
                0 if other_settings["theme"] == "light" else 1
            )
            self.main_window.push_messages = other_settings["push_messages"]
            self.main_window.logging = other_settings["logging"]

        logger.success("Завантажені інші налаштування")

    except Exception as error:
        logger.error(f"Помилка під час завантаження інших налаштуваннь: {error}")
        remove(self.other_settings.other_settings_file_path)


def save_other_settings(self) -> None:
    """Зберегти інші налаштування"""
    push_messages = self.design.push_messages.isChecked()
    logging = self.design.logging.isChecked()
    theme = "light" if self.design.new_theme.currentIndex() == 0 else "dark"
    self.other_settings.write(push_messages, logging, theme)
    self.main_window.push_messages = push_messages

    if logging:
        enable()

    else:
        disable()

    set_theme(self, theme)
    logger.success("Збережені інші налаштування")


def set_theme(self, theme):
    """Встановити тему"""
    logger.debug("set_theme")
    theme = dark if theme == "dark" else light

    self.main_window.design.setStyleSheet(theme)
    self.design.setStyleSheet(theme)
    self.add_server_window.design.setStyleSheet(theme)
