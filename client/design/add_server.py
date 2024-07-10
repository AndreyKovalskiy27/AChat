# Form implementation generated from reading ui file 'design/QtDesigner/add_server.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from os.path import join
from json import load
from PyQt6 import QtCore, QtGui, QtWidgets


class AddServerWindowDesign(object):
    def setupUi(self, MainWindow, language: str="ua"):
        self.language = language
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(410, 289)
        MainWindow.setStyleSheet("background-color: rgb(64, 65, 62); color: black;")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ip = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.ip.setGeometry(QtCore.QRect(10, 80, 391, 61))
        self.ip.setStyleSheet("background-color: rgb(229, 229, 229);\n"
"border-radius: 15px;\n"
"padding-left: 5px;\n"
"font-size: 15px")
        self.ip.setObjectName("ip")
        self.port = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.port.setGeometry(QtCore.QRect(10, 150, 391, 61))
        self.port.setStyleSheet("background-color: rgb(229, 229, 229);\n"
"border-radius: 15px;\n"
"padding-left: 5px;\n"
"font-size: 15px")
        self.port.setObjectName("port")
        self.name = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.name.setGeometry(QtCore.QRect(10, 10, 391, 61))
        self.name.setStyleSheet("background-color: rgb(229, 229, 229);\n"
"border-radius: 15px;\n"
"padding-left: 5px;\n"
"font-size: 15px")
        self.name.setObjectName("name")
        self.add_server = QtWidgets.QPushButton(parent=self.centralwidget)
        self.add_server.setGeometry(QtCore.QRect(10, 220, 391, 61))
        self.add_server.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.add_server.setStyleSheet("QPushButton {\n"
"    background-color: rgb(123, 123, 123);\n"
"    border-radius: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(108, 108, 108);\n"
"}")
        self.add_server.setObjectName("add_server")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow, language)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow, language):
        with open(join("design", "translation.json"), "r", encoding="utf-8") as translation_file:
            translation = load(translation_file)[language]

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", translation["add_server_window_title"]))
        self.ip.setPlaceholderText(_translate("MainWindow", translation["ip"]))
        self.port.setPlaceholderText(_translate("MainWindow", translation["port"]))
        self.name.setPlaceholderText(_translate("MainWindow", translation["name"]))
        self.add_server.setText(_translate("MainWindow", translation["add_server"]))
