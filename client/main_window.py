"""Модуль головного вікна"""


from PyQt6.QtWidgets import QMainWindow, QListWidgetItem
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from design import main_window
import connect_to_server_window
import messages


class MainWindow(QMainWindow):
    """Головне вікно"""
    def __init__(self) -> None:
        super().__init__()

        self.design = main_window.MainWindowDesign()
        self.design.setupUi(self)
        self.block_interface()

        self.connect_to_server_window = connect_to_server_window.ConnectToServerWindow(self)

        # Обробка нажаття на кнопки
        self.design.connect_to_server.clicked.connect(self.connect_to_server_window.show)
        self.design.send_message.clicked.connect(self.send_message)
        self.design.exit.clicked.connect(self.exit)

    def block_interface(self) -> None:
        """
        Розблоковує кнопку для підключення до серверу та
        Блокує кнопки для для відправки повідомлень, тощо
        """
        self.design.connect_to_server.setEnabled(True)
        self.design.send_message.setEnabled(False)
        self.design.message.setEnabled(False)
        self.design.messages.setEnabled(True)
        self.design.exit.setEnabled(False)

    def unblock_interface(self) -> None:
        """
        Блокує кнопку для підключення до серверу та
        розблоковує кнопки для для відправки повідомлень, тощо
        """
        self.design.connect_to_server.setEnabled(False)
        self.design.send_message.setEnabled(True)
        self.design.message.setEnabled(True)
        self.design.messages.setEnabled(True)
        self.design.exit.setEnabled(True)

    def add_message(self, text: str, bold: bool=True, font_size: int=25,
                    aligment: Qt.AlignmentFlag=Qt.AlignmentFlag.AlignHCenter) -> None:
        """Відображає повідомлення користувачу у список повідомленнь"""
        item = QListWidgetItem()
        item.setText(text)
        font = QFont()
        font.setBold(bold)
        font.setPointSize(font_size)
        item.setFont(font)
        item.setTextAlignment(aligment)
        self.design.messages.addItem(item)

    def send_message(self) -> None:
        """Відправити повідомлення"""
        message = self.design.message.text()

        if message.strip():
            try:
                self.connection.send_message({"type": "message", "message": message})
                self.add_message(f"{self.connection.nikname}: {message}",
                                False, aligment=Qt.AlignmentFlag.AlignRight)

            except:
                self.exit()
                messages.show("Не вдалося відправити повідомлення",
                              "Схоже, сервер зупинив роботу", 
                              messages.QMessageBox.Icon.Critical)
        else:
            messages.show("Не вдалося відправити повідомлення", "Повідомлення не може бути пустим")

    def exit(self) -> None:
        """Вийти з серверу"""
        try:
            self.messages_monitor.terminate()
            self.connection.exit()

        except:
            pass

        self.add_message("Ви вийшли з серверу")
        self.block_interface()
