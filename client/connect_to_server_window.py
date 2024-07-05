"""Модуль вікна підключення до сервера"""


from PyQt6.QtWidgets import QMainWindow
from design.connect_to_server import ConnectToServerWindowDesign
import messages


class ConnectToServerWindow(QMainWindow):
    """Вікно підключення до сервера"""
    def __init__(self) -> None:
        super().__init__()

        self.design = ConnectToServerWindowDesign()
        self.design.setupUi(self)

        self.design.connect_to_server.clicked.connect(self.connect_to_server)

    def connect_to_server(self) -> None:
        """Підключитися до серверу"""
        ip = self.design.ip.text()
        port = self.design.port.text()
        nikname = self.design.nikname.text()

        if ip.strip() and port.strip() and nikname.strip():
            pass

        else:
            messages.show("Введіть вірні данні",
                          "Заповніть всі поля",
                          messages.QMessageBox.Icon.Warning)
