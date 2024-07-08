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

        self.selected_sticker = None
        self.stickers = {
            1: self.design.sticker1,
            2: self.design.sticker2,
            3: self.design.sticker3,
            4: self.design.sticker4,
            5: self.design.sticker5,
            6: self.design.sticker6,
        }
        self.connect_to_server_window = connect_to_server_window.ConnectToServerWindow(self)

        # Обробка нажаття на кнопки
        self.design.connect_to_server.clicked.connect(self.connect_to_server_window.show)
        self.design.send_message.clicked.connect(self.send_message)
        self.design.exit.clicked.connect(self.exit)

        # Натискання на стікери
        self.design.sticker1.clicked.connect(lambda: self.select_sticker(1))
        self.design.sticker2.clicked.connect(lambda: self.select_sticker(2))
        self.design.sticker3.clicked.connect(lambda: self.select_sticker(3))
        self.design.sticker4.clicked.connect(lambda: self.select_sticker(4))
        self.design.sticker5.clicked.connect(lambda: self.select_sticker(5))
        self.design.sticker6.clicked.connect(lambda: self.select_sticker(6))

    def select_sticker(self, sticker_number: int) -> None:
        """Вибрати стікер"""
        if self.selected_sticker == sticker_number:
            self.stickers[sticker_number].setStyleSheet("")
            self.selected_sticker = None

        else:
            if self.selected_sticker:
                self.stickers[self.selected_sticker].setStyleSheet("")

            self.stickers[sticker_number].setStyleSheet("border-radius: 50%; border: 2px solid white;")
            self.selected_sticker = sticker_number

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
