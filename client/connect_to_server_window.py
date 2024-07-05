"""Модуль вікна підключення до сервера"""


from PyQt6.QtWidgets import QMainWindow
from design.connect_to_server import ConnectToServerWindowDesign


class ConnectToServerWindow(QMainWindow):
    """Вікно підключення до сервера"""
    def __init__(self) -> None:
        super().__init__()

        self.design = ConnectToServerWindowDesign()
        self.design.setupUi(self)
