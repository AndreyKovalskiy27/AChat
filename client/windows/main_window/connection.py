"""Функції, які відносяться до зʼєднання з сервером"""

from os.path import join
from PyQt6.QtCore import Qt
from loguru import logger
from design.utils import btn_locker
from .add_message import add_message
from design.utils import translation
import messages


def send_message(self) -> None:
    """Відправити повідомлення"""
    message = self.design.message.text()

    if message.strip():
        logger.debug(self.is_connected)
        if self.is_connected:
            try:
                if self.selected_sticker:
                    avatar = self.selected_sticker

                else:
                    if self.connect_to_server_window.avatar.has_own_avatar():
                        if self.connect_to_server_window.avatar.is_file_not_heavy(
                            self.connect_to_server_window.avatar.get_avatar_path()
                        ):
                            avatar = self.connect_to_server_window.avatar.get_avatar_encoded()

                        else:
                            avatar = None
                            messages.show(
                                translation.TRANSLATION[self.design.language][
                                    "avatar_too_heavy_error"
                                ],
                                translation.TRANSLATION[self.design.language][
                                    "avatar_too_heavy_error"
                                ],
                            )

                    else:
                        avatar = None

                logger.debug(f"AVATAR: {avatar}")

                self.connection.send_message(
                    {"type": "message", "message": message, "avatar": avatar}
                )

                sticker = (
                    join("assets", f"{self.selected_sticker}.png")
                    if isinstance(avatar, int) else avatar if avatar else join("assets", "user.png"))

                add_message(
                    self,
                    f"{self.connection.nikname} ({translation.TRANSLATION[self.design.language]["you"]}):\n{
                        message}",
                    False,
                    aligment=Qt.AlignmentFlag.AlignRight,
                    icon=sticker,
                )
                self.design.message.clear()
                logger.success("Відправлено повідомлення")

            except Exception as error:
                logger.error(f"Помилка під час надсилання повідомлення: {error}")
                exit_from_server(self)
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
                translation.TRANSLATION[self.design.language][
                    "please_connect_to_server"
                ],
                translation.TRANSLATION[self.design.language][
                    "please_connect_to_server"
                ],
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

        except Exception as error:
            logger.error(error)

    except Exception as error:
        logger.error(error)

    self.is_connected = False
    add_message(self, translation.TRANSLATION[self.design.language]["exit_message"])
    self.block_chat()
    btn_locker.unlock_btn(self.connect_to_server_window.design.connect_to_server)
    logger.success("Успішний вихід з серверу")
