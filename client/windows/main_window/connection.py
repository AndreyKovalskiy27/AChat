"""Функції, які відносяться до зʼєднання з сервером"""

from os.path import join
from PyQt6.QtCore import Qt
from loguru import logger
from design import btn_locker
from .add_message import add_message
import translation
import messages


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
            add_message(
                self,
                f"{self.connection.nikname} ({translation.TRANSLATION[self.design.language]["you"]}):\n{
                    message}",
                False,
                aligment=Qt.AlignmentFlag.AlignRight,
                icon=sticker,
            )
            logger.success("Відправлено повідомлення")

        except Exception as error:
            logger.error(f"Помилка під час надсилання повідомлення: {error}")
            self.exit_from_server()
            messages.show(
                translation.TRANSLATION[self.design.language]["sending_message_error"],
                translation.TRANSLATION[self.design.language]["sending_message_error"],
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

        except Exception as error:
            logger.error(error)

    except Exception as error:
        logger.error(error)

    add_message(self, translation.TRANSLATION[self.design.language]["exit_message"])
    self.block_chat()
    btn_locker.unlock_btn(self.connect_to_server_window.design.connect_to_server)
    logger.success("Успішний вихід з серверу")
