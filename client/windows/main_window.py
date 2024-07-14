"""Модуль головного вікна"""

from os.path import join
from PyQt6.QtWidgets import QMainWindow, QListWidgetItem
from PyQt6.QtGui import QFont, QIcon, QPixmap
from PyQt6.QtCore import Qt, QSize
from design import main_window
from design import btn_locker
from windows.connect_to_server_window import ConnectToServerWindow
from settings import Language
import messages
import translation


class MainWindow(QMainWindow):
    """Головне вікно"""

    def __init__(self) -> None:
        super().__init__()

        language = Language().get()

        self.design = main_window.MainWindowDesign()
        self.design.setupUi(self, language)
        self.design.messages.setIconSize(QSize(70, 70))
        self.block_chat()

        self.selected_sticker = None
        self.stickers = {
            1: self.design.sticker1,
            2: self.design.sticker2,
            3: self.design.sticker3,
            4: self.design.sticker4,
            5: self.design.sticker5,
            6: self.design.sticker6,
            7: self.design.sticker7,
            8: self.design.sticker8,
            9: self.design.sticker9,
            10: self.design.sticker10,
            11: self.design.sticker11,
            12: self.design.sticker12,
            13: self.design.sticker13,
            14: self.design.sticker14,
            15: self.design.sticker15
        }
        self.connect_to_server_window = ConnectToServerWindow(self, language)

        # Обробка нажаття на кнопки
        self.design.connect_to_server.clicked.connect(
            self.connect_to_server_window.show
        )
        self.design.send_message.clicked.connect(self.send_message)
        self.design.exit.clicked.connect(self.exit_from_server)

        # Натискання на стікери
        self.design.sticker1.clicked.connect(lambda: self.select_sticker(1))
        self.design.sticker2.clicked.connect(lambda: self.select_sticker(2))
        self.design.sticker3.clicked.connect(lambda: self.select_sticker(3))
        self.design.sticker4.clicked.connect(lambda: self.select_sticker(4))
        self.design.sticker5.clicked.connect(lambda: self.select_sticker(5))
        self.design.sticker6.clicked.connect(lambda: self.select_sticker(6))
        self.design.sticker7.clicked.connect(lambda: self.select_sticker(7))
        self.design.sticker8.clicked.connect(lambda: self.select_sticker(8))
        self.design.sticker9.clicked.connect(lambda: self.select_sticker(9))
        self.design.sticker10.clicked.connect(lambda: self.select_sticker(10))
        self.design.sticker11.clicked.connect(lambda: self.select_sticker(11))
        self.design.sticker12.clicked.connect(lambda: self.select_sticker(12))
        self.design.sticker13.clicked.connect(lambda: self.select_sticker(13))
        self.design.sticker14.clicked.connect(lambda: self.select_sticker(14))
        self.design.sticker15.clicked.connect(lambda: self.select_sticker(15))

    def select_sticker(self, sticker_number: int) -> None:
        """Вибрати стікер"""
        if self.selected_sticker == sticker_number:
            self.stickers[sticker_number].setStyleSheet("")
            self.selected_sticker = None

        else:
            if self.selected_sticker:
                self.stickers[self.selected_sticker].setStyleSheet("")

            self.stickers[sticker_number].setStyleSheet(
                "border-radius: 50%; border: 2px solid white;"
            )
            self.selected_sticker = sticker_number

    def block_chat(self) -> None:
        """Заблокувати чат (кнопки для відправки повідомлення та виходу з сервера)"""
        btn_locker.lock_btn(self.design.send_message)
        btn_locker.lock_btn(self.design.exit)

    def unblock_chat(self) -> None:
        """Розблокувати чат (кнопки для відправки повідомлення та виходу з сервера)"""
        btn_locker.unlock_btn(self.design.send_message)
        btn_locker.unlock_btn(self.design.exit)

    def add_message(
        self,
        text: str,
        bold: bool = True,
        font_size: int = 25,
        aligment: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignCenter,
        icon: str = None,
    ) -> None:
        """Відображає повідомлення користувачу у список повідомленнь"""
        item = QListWidgetItem()
        item.setTextAlignment(aligment)
        item.setText(text)
        font = QFont()
        font.setBold(bold)
        font.setPointSize(font_size)
        item.setFont(font)

        if icon:
            if isinstance(icon, bytes):
                pixmap = QPixmap()
                pixmap.loadFromData(icon)
                item.setIcon(QIcon(pixmap))

            else:
                item.setIcon(QIcon(icon))

        self.design.messages.addItem(item)
        self.design.messages.scrollToBottom()  # Автоскролл

    def send_message(self) -> None:
        """Відправити повідомлення"""
        message = self.design.message.text()

        if message.strip():
            try:
                self.connection.send_message(
                    {
                        "type": "message",
                        "message": message,
                        "avatar": self.selected_sticker
                        if self.selected_sticker
                        else self.connect_to_server_window.avatar.get_avatar_encoded()
                        if self.connect_to_server_window.avatar.has_own_avatar()
                        else None,
                    }
                )

                sticker = (
                    join("assets", f"{self.selected_sticker}.png")
                    if self.selected_sticker
                    else self.connect_to_server_window.avatar.get_avatar_path()
                )
                self.add_message(
                    f"{self.connection.nikname} ({translation.TRANSLATION[self.design.language]["you"]}):\n{message}",
                    False,
                    aligment=Qt.AlignmentFlag.AlignRight,
                    icon=sticker,
                )

            except Exception as error:
                self.exit_from_server()
                messages.show(
                    translation.TRANSLATION[self.design.language][
                        "sending_message_error"
                    ],
                    translation.TRANSLATION[self.design.language][
                        "sending_message_error"
                    ],
                    messages.QMessageBox.Icon.Critical,
                    error,
                )
        else:
            messages.show(
                translation.TRANSLATION[self.design.language]["message_empty"],
                translation.TRANSLATION[self.design.language]["message_empty"],
            )

    def exit_from_server(self) -> None:
        """Вийти з серверу"""
        try:
            self.messages_monitor.quit()

            try:
                self.connection.send_message({"type": "exit"})
                self.connection.connection_socket.close()

            except Exception:
                pass

        except Exception:
            pass

        self.add_message(translation.TRANSLATION[self.design.language]["exit_message"])
        self.block_chat()
        btn_locker.unlock_btn(self.connect_to_server_window.design.connect_to_server)

    def closeEvent(self, a0) -> None:
        """
        Цей код виконується під час виходу з программи
        В данному випадку виконується автоматичний вихід з серверу
        """
        self.exit_from_server()
        a0.accept()
