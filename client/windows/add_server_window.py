"""Вікно додавання сервера"""


import translation
from PyQt6.QtWidgets import QMainWindow
from design import add_server
from settings import Servers
import messages


class AddServerWindow(QMainWindow):
    """Вікно додавання сервера"""
    def __init__(self, connect_to_server_window: QMainWindow) -> None:
        super().__init__(connect_to_server_window)

        self.connect_to_server_window = connect_to_server_window

        self.design = add_server.AddServerWindowDesign()
        self.design.setupUi(self)

        self.servers = Servers()

        self.design.add_server.clicked.connect(self.add_server)

    def add_server(self) -> None:
        """Додати сервер"""
        name = self.design.name.text()
        ip = self.design.ip.text()
        port = self.design.port.text()

        if name.strip() and ip.strip() and port.strip():
            if port.isdecimal():
                try:
                    self.servers.add_server(name, ip, int(port))
                    self.close()

                except Exception as error:
                    messages.show(translation.TRANSLATION[self.design.language]["server_add_error"],
                                  translation.TRANSLATION[self.design.language]["server_add_error"],
                                  messages.QMessageBox.Icon.Critical, error)

                finally:
                    self.connect_to_server_window.load_servers()

            else:
                messages.show("Введіть вірні данні", "Порт повинен бути числом")

        else:
            messages.show("Введіть вірні данні", "Заповніть всі поля")
