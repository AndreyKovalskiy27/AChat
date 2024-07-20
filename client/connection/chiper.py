"""Шифрувальник"""

from typing import Any
from pickle import dumps, loads
from cryptography.fernet import Fernet
from loguru import logger


class Chiper:
    """Шифрувальник"""

    def __init__(self, key) -> None:
        self.chiper = Fernet(key)
        logger.success("Ініціалізован шифрувальник")

    def encrypt(self, data: Any) -> bytes:
        """Зашифрувати данні"""
        encrypted = self.chiper.encrypt(dumps(data))
        logger.debug(f"Зашифровано повідомлення: {encrypted}")
        return encrypted

    def decrypt(self, encrypted: bytes) -> Any:
        """Розшифрувати данні"""
        decrypted = loads(self.chiper.decrypt(encrypted))
        logger.debug("Розшифровано повідомлення: ######")
        return decrypted
