"""Обробник нового повідомлення"""


from os.path import join, exists
from base64 import b64decode
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt
import translation


def message_handler(data: dict, main_window) -> None:
    """Обробник нового повідомлення"""
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

    main_window.add_message(
        text,
        False,
        aligment=Qt.AlignmentFlag.AlignLeft,
        icon=avatar,
    )


    # Push-повідомлення
    icon = avatar

    if isinstance(icon, bytes):
        icon = QPixmap()
        icon.loadFromData(icon)
        icon = QIcon(icon)

    else:
        icon = QIcon(icon)

    if not main_window.isActiveWindow():
        main_window.tray_icon.showMessage(
            data["nikname"],
            data["message"],
            icon,
            3000
        )