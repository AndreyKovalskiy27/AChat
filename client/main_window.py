"""Модуль головного вікна"""


from PyQt6.QtWidgets import QMainWindow
from design import main_window
import connect_to_server_window


class MainWindow(QMainWindow):
    """Головне вікно"""
    def __init__(self) -> None:
        super().__init__()

        self.design = main_window.MainWindowDesign()
        self.design.setupUi(self)

        self.connect_to_server_window = connect_to_server_window.ConnectToServerWindow()

        # Обробка нажаття на кнопки
        self.design.connect_to_server.clicked.connect(self.connect_to_server_window.show)
