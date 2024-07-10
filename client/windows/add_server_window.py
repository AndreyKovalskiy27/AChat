"""Вікно додавання сервера"""


from PyQt6.QtWidgets import QMainWindow
from design import add_server


class AddServerWindow(QMainWindow):
    """Вікно додавання сервера"""
    def __init__(self) -> None:
        super().__init__(None)

        self.design = add_server.AddServerWindowDesign()
        self.design.setupUi(self)
