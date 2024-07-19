"""Моніторинг повідомленнь від сервера"""

from os.path import join, exists
from base64 import b64decode
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt, QThread
from connection.connection import Connection
import translation
import traceback


class MessagesMonitor(QThread):
    """Монітогинг повідомленнь від сервера та вивід на єкран"""

    def __init__(self, connection: Connection, main_window) -> None:
        super().__init__()
        self.connection = connection
        self.main_window = main_window

    def run(self) -> None:
        """Запустити монітогинг повідомленнь від сервера та вивід на єкран"""
        self.connection.connection_socket.settimeout(None)

        while True:
            try:
                data = self.connection.get_data_from_server()

                if data["type"] == "message":
                    avatar = data.get("avatar", join("assets", "error.png"))

                    if avatar:
                        # Якщо був відправлений смайлик
                        if isinstance(avatar, int):
                            avatar = (
                                join("assets", f"{data["avatar"]}.png")
                                if avatar
                                else None
                            )

                            if not exists(avatar):
                                avatar = join("assets", "error.png")

                        # Якщо була відправлена аватарка
                        elif isinstance(avatar, bytes):
                            try:
                                avatar = b64decode(avatar)

                            except Exception:
                                avatar = join("assets", "error.png")

                    else:
                        avatar = join("assets", "user.png")

                    text = f"{data["nikname"]}:\n{data["message"]}"

                    self.main_window.add_message(
                        text,
                        False,
                        aligment=Qt.AlignmentFlag.AlignLeft,
                        icon=avatar,
                    )

                    icon = avatar

                    if isinstance(icon, bytes):
                        icon = QPixmap()
                        icon.loadFromData(icon)
                        icon = QIcon(icon)

                    else:
                        icon = QIcon(icon)

                    if not self.main_window.isActiveWindow():
                        self.main_window.tray_icon.showMessage(
                            data["nikname"],
                            data["message"],
                            icon,
                            3000
                        )

                elif data["type"] == "new_user":
                    text = (f"{data["nikname"]} {translation.TRANSLATION[
                        self.main_window.design.language][
                        "new_user_connected"]}")
                    self.main_window.add_message(text)

                    if not self.main_window.isActiveWindow():
                        self.main_window.tray_icon.showMessage(
                            text,
                            "",
                            self.main_window.tray_icon.MessageIcon.NoIcon,
                            3000)

                elif data["type"] == "exit":
                    text = (f"{data["nikname"]} "
                            f"{translation.TRANSLATION[
                                self.main_window.design.language][
                                "user_exited"]}")
                    was_error = data.get("was_error", False)

                    if was_error:
                        text = (f"{data["nikname"]} "
                        f"{translation.TRANSLATION[
                            self.main_window.design.language][
                            "user_deleted_by_an_error"]}")

                    self.main_window.add_message(text)

                    if not self.main_window.isActiveWindow():
                        self.main_window.tray_icon.showMessage(
                            text,
                            "",
                            self.main_window.tray_icon.MessageIcon.NoIcon,
                            3000)

            except Exception:
                traceback.print_exc()
