"""Вікно додавання сервера"""


from PyQt6.QtWidgets import QMainWindow
from design import add_server
from settings import Servers
import messages


class AddServerWindow(QMainWindow):
    """Вікно додавання сервера"""
    def __init__(self, parent: QMainWindow) -> None:
        super().__init__(parent)

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
                    self.servers.add_server(name, ip, port)
                    self.close()

                except Exception as error:
                    messages.show("Помилка", "Не вдалося створити сервер",
                                  messages.QMessageBox.Icon.Critical, error)

            else:
                messages.show("Введіть вірні данні", "Порт повинен бути числом")

        else:
            messages.show("Введіть вірні данні", "Заповніть всі поля")
