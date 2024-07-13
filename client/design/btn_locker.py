"""Заблокувати кнопки"""


from PyQt6.QtWidgets import QPushButton


NORMAL_STYLE = """
QPushButton {
	background-color: rgb(123, 123, 123);
	border-radius: 15px;
}
QPushButton:hover {
	background-color: rgb(108, 108, 108);
}
"""

LOCKED_STYLE = """
background-color: rgb(80, 80, 80);
border-radius: 15px;
"""


def lock_btn(btn: QPushButton) -> None:
    """Заблокувати кнопку"""
    btn.setEnabled(False)
    btn.setStyleSheet(LOCKED_STYLE)

def unlock_btn(btn: QPushButton) -> None:
    """Розблокувати кнопку"""
    btn.setEnabled(True)
    btn.setStyleSheet(NORMAL_STYLE)
