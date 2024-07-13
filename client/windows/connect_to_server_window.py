"""Модуль вікна підключення до сервера"""

from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QFileDialog
from PyQt6.QtGui import QPixmap
from design.connect_to_server import ConnectToServerWindowDesign
from windows.add_server_window import AddServerWindow
from connection.messages_monitor import MessagesMonitor
from connection.connection_thread import ConnectionThread
from connection.connection import Connection
import settings
import messages
import translation


class ConnectToServerWindow(QMainWindow):
    """Вікно підключення до сервера"""

    def __init__(self, main_window, language: str = "ua") -> None:
        super().__init__(main_window)

        self.design = ConnectToServerWindowDesign()
        self.design.setupUi(self, language)

        self.connection_data = settings.ConnectionData()
        self.servers = settings.Servers()
        self.language = settings.Language()
        self.avatar = settings.UserAvatar()

        self.main_window = main_window
        self.language_codes = {"Українська": "ua", "English": "en"}
        self.add_server_window = AddServerWindow(self, language)
        self.design.new_language.setCurrentText(
            dict(zip(self.language_codes.values(), self.language_codes.keys()))[
                self.language.get()
            ]
        )
        self.load_connection_data()
        self.load_servers()

        # Натискання на кнопки
        self.design.connect_to_server.clicked.connect(self.connect_to_server)
        self.design.save.clicked.connect(self.save_connection_data)
        self.design.add_server.clicked.connect(self.add_server_window.show)
        self.design.delete_server.clicked.connect(self.delete_server)
        self.design.apply_server.clicked.connect(self.apply_server)
        self.design.set_language.clicked.connect(self.set_language)
        self.design.load_avatar.clicked.connect(self.set_avatar)

    def check_not_empty(self) -> tuple:
        """Перевірити, чи заповнив користувач форму для підключення до серверу"""
        ip = self.design.ip.text()
        port = self.design.port.text()
        nikname = self.design.nikname.text()

        if ip.strip() and port.strip() and nikname.strip():
            if port.isdecimal():
                return ip, int(port), nikname

            else:
                messages.show(
                    translation.TRANSLATION[self.design.language][
                        "port_must_be_number"
                    ],
                    translation.TRANSLATION[self.design.language][
                        "port_must_be_number"
                    ],
                )

        else:
            messages.show(
                translation.TRANSLATION[self.design.language]["enter_all_fields"],
                translation.TRANSLATION[self.design.language]["enter_all_fields"],
            )

    def connection_signal_handler(self, value) -> None:
        """Обробник сигналів з потока підключення до сервера"""
        if isinstance(value, Connection):
            self.main_window.connection = value
            self.main_window.messages_monitor = MessagesMonitor(
                self.main_window.connection, self.main_window
            )
            self.main_window.messages_monitor.start()

            self.close()
            self.design.connect_to_server.setEnabled(False)
            self.main_window.design.messages.clear()
            self.main_window.unblock_chat()
            self.main_window.add_message(
                translation.TRANSLATION[self.design.language]["connection_message"]
            )
            self.connection_thread.terminate()

        else:
            messages.show(
                translation.TRANSLATION[self.design.language][
                    "connection_to_server_error"
                ],
                translation.TRANSLATION[self.design.language][
                    "connection_to_server_error"
                ],
                messages.QMessageBox.Icon.Critical,
                value,
            )

    def connect_to_server(self) -> None:
        """Підключитися до серверу"""
        form_data = self.check_not_empty()

        if form_data:
            self.connection_thread = ConnectionThread(
                form_data[0], form_data[1], form_data[2]
            )
            self.connection_thread.signal.connect(self.connection_signal_handler)
            self.connection_thread.start()

    def save_connection_data(self) -> None:
        """Зберегти данні для підключення до серверу"""
        form_data = self.check_not_empty()

        if form_data:
            self.connection_data.write(form_data[0], form_data[1], form_data[2])

    def load_connection_data(self) -> None:
        """Завантажити данні для підключення до серверу"""
        try:
            connection_data_json = self.connection_data.read()

            if connection_data_json:
                self.design.ip.setText(connection_data_json["ip"])
                self.design.port.setText(str(connection_data_json["port"]))
                self.design.nikname.setText(connection_data_json["nikname"])

        except Exception:
            settings.remove(self.connection_data.connection_data_file_path)

    def load_servers(self) -> None:
        """Завантажити сервери"""
        try:
            servers = self.servers.get_servers()
            self.design.servers.setRowCount(len(servers.keys()))
            row = 0

            for server in servers.keys():
                self.design.servers.setItem(row, 0, QTableWidgetItem(server))
                self.design.servers.setItem(
                    row, 1, QTableWidgetItem(servers[server]["ip"])
                )
                self.design.servers.setItem(
                    row, 2, QTableWidgetItem(str(servers[server]["port"]))
                )
                row += 1

        except Exception:
            settings.remove(self.servers.servers_file_path)

    def apply_server(self) -> None:
        """Встановити IP та порт вибранного сервера"""
        row = self.design.servers.currentRow()

        if row > -1:
            self.design.ip.setText(self.design.servers.item(row, 1).text())
            self.design.port.setText(self.design.servers.item(row, 2).text())

    def delete_server(self) -> None:
        """Видалити сервер"""
        row = self.design.servers.currentRow()

        if row > -1:
            try:
                server_name = self.design.servers.item(row, 0).text()
                self.servers.delete_server(server_name)
                self.load_servers()

            except Exception as error:
                self.load_servers()
                messages.show(
                    translation.TRANSLATION[self.design.language][
                        "server_deletion_error"
                    ],
                    translation.TRANSLATION[self.design.language][
                        "server_deletion_error"
                    ],
                    messages.QMessageBox.Icon.Critical,
                    error,
                )

    def set_language(self) -> None:
        """Встановити мову"""
        new_language = self.language_codes[self.design.new_language.currentText()]

        self.main_window.design.language = new_language
        self.design.language = new_language
        self.add_server_window.design.language = new_language

        self.main_window.design.retranslateUi(self.main_window, new_language)
        self.design.retranslateUi(self, new_language)
        self.add_server_window.design.retranslateUi(
            self.add_server_window, new_language
        )
        self.language.write(new_language)

    def set_avatar(self) -> None:
        """Встановити аватар"""
        new_avatar_file_path = QFileDialog(
            self, None, None, "Image (*.png *.jpg);"
        ).getOpenFileName()[0]

        if new_avatar_file_path:
            self.avatar.set_avatar(new_avatar_file_path)
            self.design.avatar.setPixmap(QPixmap(new_avatar_file_path))
