"""Модуль для показу соповіщень на єкран"""

from PyQt6.QtWidgets import QMessageBox


def show(
    message: str,
    description: str = None,
    icon: QMessageBox.Icon = None,
    detailed_text: str = None,
) -> None:
    """Показує повідомлення"""
    qmessagebox = QMessageBox()

    if icon:
        qmessagebox.setIcon(icon)

    qmessagebox.setWindowTitle(message)
    qmessagebox.setText(description)

    if detailed_text:
        qmessagebox.setDetailedText(str(detailed_text))

    qmessagebox.exec()
