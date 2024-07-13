"""Вікно додавання сервера"""

import translation
from PyQt6.QtWidgets import QMainWindow
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

        self.design.add_server.clicked.connect(self.add_server)

    def add_server(self) -> None:
        """Додати сервер"""
        name = self.design.name.text()
        ip = self.design.ip.text()
        port = self.design.port.text()

        if name.strip() and ip.strip() and port.strip():
            if port.isdecimal():
                try:
                    self.servers.add_server(name, ip, int(port))
                    self.close()

                except Exception as error:
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
