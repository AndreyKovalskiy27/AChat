"""Обробка кнопок для роботи з данними для підключення до сервера"""

import re
from typing import Union
from os import remove
from loguru import logger
import messages
from design.utils import translation as translation


def check_data(self, check_data=True) -> Union[tuple, None]:
    """Перевірити, чи правильно користувач заповнив форму для підключення до серверу"""
    ip = self.design.ip.text()
    port = self.design.port.text()
    nikname = self.design.nikname.text()

    if not check_data or (ip.strip() and port.strip() and nikname.strip()):
        if check_data:
            if port.isdecimal():
                port = int(port)

                if port >= 0 and port <= 65535:
                    pattern = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
                    is_ip_valid = re.match(pattern, ip) is not None

                    if is_ip_valid:
                        return ip, port, nikname

                    else:
                        messages.show(
                            translation.TRANSLATION[self.design.language][
                                "incorrect_ip_error"
                            ],
                            translation.TRANSLATION[self.design.language][
                                "incorrect_ip_error"
                            ],
                        )

                else:
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
            return ip, port, nikname

    else:
        messages.show(
            translation.TRANSLATION[self.design.language]["enter_all_fields"],
            translation.TRANSLATION[self.design.language]["enter_all_fields"],
        )


def save_connection_data(self) -> None:
    """Зберегти данні для підключення до серверу"""
    form_data = check_data(self, False)

    if form_data:
        self.connection_data.write(form_data[0], form_data[1], form_data[2])
        logger.success("Данні для підключення до серверу збережені")


def load_connection_data(self) -> None:
    """Завантажити данні для підключення до серверу"""
    try:
        connection_data_json = self.connection_data.read()

        if connection_data_json:
            self.design.ip.setText(connection_data_json["ip"])
            self.design.port.setText(str(connection_data_json["port"]))
            self.design.nikname.setText(connection_data_json["nikname"])

        logger.success("Завантаженні данні для підключення до серверу")

    except Exception as error:
        logger.error(
            f"Помилка під час завантаження данних для підключення до серверу: {error}"
        )
        remove(self.connection_data.connection_data_file_path)
