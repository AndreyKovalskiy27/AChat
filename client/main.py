"""Головний модуль. Запускає программу"""

import sys
from PyQt6.QtWidgets import QApplication
from windows import main_window

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = main_window.MainWindow()
    window.show()
    app.exec()
