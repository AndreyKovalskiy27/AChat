"""Модуль вікна підключення до сервера"""


from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QAbstractItemView
from design.connect_to_server import ConnectToServerWindowDesign
from windows.add_server_window import AddServerWindow
from connection.messages_monitor import MessagesMonitor
from connection.connection_thread import ConnectionThread
from connection.connection import Connection
import settings
import messages


class ConnectToServerWindow(QMainWindow):
    """Вікно підключення до сервера"""
    def __init__(self, main_window) -> None:
        super().__init__(main_window)

        self.design = ConnectToServerWindowDesign()
        self.design.setupUi(self)

        # Налаштування таблиці серверів
        self.design.servers.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.design.servers.setColumnCount(3)
        self.design.servers.setHorizontalHeaderLabels(["Назва", "IP", "Порт"])

        for column in range(3):
            self.design.servers.setColumnWidth(column, self.design.servers.width() // 3)

        self.main_window = main_window
        self.add_server_window = AddServerWindow(self)
        self.connection_data = settings.ConnectionData()
        self.servers = settings.Servers()
        self.load_connection_data()
        self.load_servers()

        # Натискання на кнопки
        self.design.connect_to_server.clicked.connect(self.connect_to_server)
        self.design.save.clicked.connect(self.save_connection_data)

        self.design.add_server.clicked.connect(self.add_server_window.show)

    def check_not_empty(self) -> None:
        """Перевірити, чи заповнив користувач форму для підключення до серверу"""
        ip = self.design.ip.text()
        port = self.design.port.text()
        nikname = self.design.nikname.text()

        if ip.strip() and port.strip() and nikname.strip():
            if port.isdecimal():
                return ip, int(port), nikname

            else:
                messages.show("Введіть вірні данні",
                          "Порт повинен бути числом")

        else:
            messages.show("Введіть вірні данні",
                          "Заповніть всі поля")

    def connection_signal_handler(self, value) -> None:
        """Обробник сигналів з потока підключення до сервера"""
        if isinstance(value, Connection):
            self.main_window.connection = value
            self.main_window.messages_monitor = MessagesMonitor(self.main_window.connection,
                                                                self.main_window)
            self.main_window.messages_monitor.start()

            self.close()
            self.block_connection_form()
            self.main_window.design.messages.clear()
            self.main_window.unblock_chat()
            self.main_window.add_message("Ви успішно підключилися до серверу")
            self.connection_thread.terminate()

        else:
            messages.show("Не вдалося доєднатися до сервера",
                        "Не вдалося доєднатися до сервера. Перевірте IP та порт",
                        messages.QMessageBox.Icon.Critical, value)

    def connect_to_server(self) -> None:
        """Підключитися до серверу"""
        form_data = self.check_not_empty()

        if form_data:
            self.connection_thread = ConnectionThread(form_data[0], form_data[1], form_data[2])
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

        except Exception as error:
            settings.remove(self.connection_data.connection_data_file_path)
            messages.show("Помилка",
                          "Не вдалося завантажити ваші налаштування. Схоже, файл "\
                          "налаштуваннь був пошкодженний. Файл налаштуваннь був видалений",
                          messages.QMessageBox.Icon.Critical,
                          error)

    def load_servers(self) -> None:
        """Завантажити сервери"""
        try:
            servers = self.servers.get_servers()
            self.design.servers.setRowCount(len(servers.keys()))
            row = 0

            for server in servers.keys():
                self.design.servers.setItem(row, 0, QTableWidgetItem(server))
                self.design.servers.setItem(row, 1, QTableWidgetItem(servers[server]["ip"]))
                self.design.servers.setItem(row, 2, QTableWidgetItem(servers[server]["port"]))
                row += 1

        except Exception as error:
            settings.remove(self.servers.servers_file_path)
            messages.show("Помилка", "Не вдалося завантажити список ваших серверів",
                          messages.QMessageBox.Icon.Critical, error)

    def block_connection_form(self) -> None:
        """Заблокувати форму для підключення до сервера"""
        self.design.ip.setEnabled(False)
        self.design.port.setEnabled(False)
        self.design.nikname.setEnabled(False)
        self.design.connect_to_server.setEnabled(False)

    def unblock_connection_form(self) -> None:
        """Розблокувати форму для підключення до сервера"""
        self.design.ip.setEnabled(True)
        self.design.port.setEnabled(True)
        self.design.nikname.setEnabled(True)
        self.design.connect_to_server.setEnabled(True)
