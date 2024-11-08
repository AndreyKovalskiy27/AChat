"""Шифрувальник"""

from typing import Any
from pickle import dumps, loads
from cryptography.fernet import Fernet


class Chiper:
    """Шифрувальник"""

    def __init__(self) -> None:
        self.key_str = Fernet.generate_key()
        self.chiper = Fernet(self.key_str)

    def encrypt(self, data: Any) -> bytes:
        """Зашифрувати данні"""
        return self.chiper.encrypt(dumps(data))

    def decrypt(self, data: bytes) -> Any:
        """Розшифрувати данні"""
        return loads(self.chiper.decrypt(data))
