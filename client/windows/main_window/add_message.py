"""Функція для додавання повідомлення у список повідомленнь"""

from PyQt6.QtWidgets import QListWidgetItem
from PyQt6.QtGui import QFont, QPixmap, QIcon
from PyQt6.QtCore import Qt


def add_message(
    self,
    text: str,
    bold: bool = True,
    font_size: int = 25,
    aligment: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignCenter,
    icon: str = None,
) -> None:
    """Відображає повідомлення користувачу у список повідомленнь"""
    item = QListWidgetItem()
    item.setTextAlignment(aligment)
    item.setText(text)
    font = QFont()
    font.setBold(bold)
    font.setPointSize(font_size)
    item.setFont(font)

    if icon:
        if isinstance(icon, bytes):
            pixmap = QPixmap()
            pixmap.loadFromData(icon)
            item.setIcon(QIcon(pixmap))

        else:
            item.setIcon(QIcon(icon))

    self.design.messages.addItem(item)
    self.design.messages.scrollToBottom()  # Автоскролл
