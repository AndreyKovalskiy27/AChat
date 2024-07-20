"""Поток для підключення до серверу"""

from PyQt6.QtCore import QThread, pyqtSignal
from connection.connection import Connection
from loguru import logger


class ConnectionThread(QThread):
    """
    Поток для підключення до серверу
    Потрібен для того, щоб підключитися до серверу на фоні,
    без зависання інтерфейсу
    """

    signal = pyqtSignal(object)

    def __init__(self, ip: str, port: int, nikname: str) -> None:
        super().__init__()
        self.ip = ip
        self.port = port
        self.nikname = nikname
        logger.success("Ініціалізован поток підключення до серверу")

    def run(self) -> None:
        try:
            connection = Connection(self.ip, self.port, self.nikname)
            self.signal.emit(connection)

        except TimeoutError:
            self.signal.emit("Server not answering more than 3 seconds")
            logger.error(
                "Помилка під час підключення до сервера: сервер не відповідає більше 3 секунд"
            )

        except Exception as error:
            self.signal.emit(str(error))
            logger.error(f"Помилка під час підключення до сервера: {error}")
