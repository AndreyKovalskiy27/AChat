"""Моніторинг повідомленнь від сервера"""


from os.path import join
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
            try:
                data = self.connection.get_data_from_server()
                print(data)

                if data["type"] == "message":
                    sticker = data.get("sticker", None)

                    if sticker:
                        sticker = join("assets", str(f"{sticker}.png"))
                    self.main_window.add_message(f"{data["nikname"]}: {data["message"]}",
                                            False, aligment=Qt.AlignmentFlag.AlignLeft,
                                            icon=sticker)

                elif data["type"] == "new_user":
                    self.main_window.add_message(f"{data["nikname"]} приєднався до чату")

                elif data["type"] == "exit":
                    self.main_window.add_message(f"{data["nikname"]} вийшов з чату")

            except:
                break
