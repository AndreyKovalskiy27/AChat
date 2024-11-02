"""Вікно додавання сервера"""

from design.utils import translation as translation
from PyQt6.QtWidgets import QMainWindow
from loguru import logger
from design import add_server
from settings import Servers
from .connect_to_server_window.servers import load_servers
import messages


class AddServerWindow(QMainWindow):
    """Вікно додавання сервера"""

    def __init__(
        self, connect_to_server_window: QMainWindow, language: str = "ua"
    ) -> None:
        super().__init__(connect_to_server_window)

        self.connect_to_server_window = connect_to_server_window

        self.design = add_server.AddServerWindowDesign()
        self.design.setupUi(self, language)

        self.servers = Servers()

        self.setup_buttons()
        logger.success("Ініціалізовано вікно додавання сервера")

    def setup_buttons(self):
        """Налаштувати обробники кнопок"""
        self.design.add_server.clicked.connect(self.add_server)

    def add_server(self) -> None:
        """Додати сервер"""
        name = self.design.name.text()
        ip = self.design.ip.text()
        port = self.design.port.text()

        if name.strip() and ip.strip() and port.strip():
            if port.isdecimal():
                port = int(port)

                if port >= 0 and port <= 65535:
                    try:
                        self.servers.add_server(name, ip, int(port))
                        logger.success("Доданий новий сервер")
                        self.close()

                    except Exception as error:
                        logger.error(
                            f"Помилка під час додавання нового сервера: {error}"
                        )
                        messages.show(
                            translation.TRANSLATION[self.design.language][
                                "server_add_error"
                            ],
                            translation.TRANSLATION[self.design.language][
                                "server_add_error"
                            ],
                            messages.QMessageBox.Icon.Critical,
                            error,
                        )

                    finally:
                        load_servers(self.connect_to_server_window)

                messages.show(
                    translation.TRANSLATION[self.design.language]["port_range_error"],
                    translation.TRANSLATION[self.design.language]["port_range_error"],
                )

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
