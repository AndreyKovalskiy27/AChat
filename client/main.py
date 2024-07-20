"""Головний модуль. Запускає программу"""

import sys
from PyQt6.QtWidgets import QApplication
from windows.main_window import main_window
from logger import enable, disable
from settings import OtherSettings


if __name__ == "__main__":
    try:
        logging = OtherSettings().get()["logging"]

        if logging:
            enable()

        else:
            disable()

    except Exception:
        pass

    app = QApplication(sys.argv)
    window = main_window.MainWindow()
    window.show()
    app.exec()
