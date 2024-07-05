"""Модуль вікна підключення до сервера"""


from PyQt6.QtWidgets import QMainWindow, QListWidgetItem
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from design.connect_to_server import ConnectToServerWindowDesign
from connection.connection import Connection
import messages


class ConnectToServerWindow(QMainWindow):
    """Вікно підключення до сервера"""
    def __init__(self, main_window) -> None:
        super().__init__(main_window)
        self.main_window = main_window

        self.design = ConnectToServerWindowDesign()
        self.design.setupUi(self)

        self.design.connect_to_server.clicked.connect(self.connect_to_server)

    def connect_to_server(self) -> None:
        """Підключитися до серверу"""
        ip = self.design.ip.text()
        port = self.design.port.text()
        nikname = self.design.nikname.text()

        if ip.strip() and port.strip() and nikname.strip():
            if port.isdecimal():
                try:
                    connection = Connection(ip, int(port), nikname)
                    self.main_window.unblock_interface()
                    self.main_window.connection = connection

                    self.main_window.design.messages.clear()
                    self.main_window.add_message("Ви успішно підключилися до серверу")

                except Exception as error:
                    messages.show("Не вдалося доєднатися до сервера",
                                "Не вдалося доєднатися до сервера. Перевірте IP та порт",
                                messages.QMessageBox.Icon.Critical, error)

            else:
                messages.show("Введіть вірні данні",
                              "Порт повинен бути числом")
        else:
            messages.show("Введіть вірні данні",
                          "Заповніть всі поля")
