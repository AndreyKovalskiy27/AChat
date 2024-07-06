"""Моніторинг повідомленнь від сервера"""


from PyQt6.QtCore import Qt, QThread, pyqtSignal
from connection.connection import Connection


class MessagesMonitor(QThread):
    """Монітогинг повідомленнь від сервера та вивід на єкран"""
    def __init__(self, connection: Connection, main_window) -> None:
        super().__init__()
        self.connection = connection
        self.main_window = main_window

    def run(self) -> None:
        """Запустити монітогинг повідомленнь від сервера та вивід на єкран"""
        while True:
            data = self.connection.get_data_from_server()

            if data["type"] == "message":
                self.main_window.add_message(f"{data["nikname"]}: {data["message"]}",
                                        False, aligment=Qt.AlignmentFlag.AlignLeft)

            elif data["type"] == "new_user":
                self.main_window.add_message(f"{data["nikname"]} приєднався до чату")

            elif data["type"] == "exit":
                self.main_window.add_message(f"{data["nikname"]} вийшов з чату")
