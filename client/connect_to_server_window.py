"""Модуль вікна підключення до сервера"""


from PyQt6.QtWidgets import QMainWindow
from design.connect_to_server import ConnectToServerWindowDesign
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

        self.main_window = main_window
        self.settings = settings.Settings()
        self.load_settings()

        # Натискання на кнопки
        self.design.connect_to_server.clicked.connect(self.connect_to_server)
        self.design.save.clicked.connect(self.save_settings)

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

    def save_settings(self) -> None:
        """Зберегти налаштування"""
        form_data = self.check_not_empty()

        if form_data:
            self.settings.write({
                "ip": form_data[0],
                "port": form_data[1],
                "nikname": form_data[2]
            })

    def load_settings(self) -> None:
        """Завантажити налаштування"""
        try:
            settings_json = self.settings.read()

            if settings_json:
                self.design.ip.setText(settings_json["ip"])
                self.design.port.setText(str(settings_json["port"]))
                self.design.nikname.setText(settings_json["nikname"])

        except Exception as error:
            settings.remove(self.settings.settings_file)
            messages.show("Помилка",
                          "Не вдалося завантажити ваші налаштування. Схоже, файл "\
                          "налаштуваннь був пошкодженний. Файл налаштуваннь був видалений",
                          messages.QMessageBox.Icon.Critical,
                          error)

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
