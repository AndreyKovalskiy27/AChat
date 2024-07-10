# Form implementation generated from reading ui file 'design/QtDesigner/connect_to_server.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from json import load
from os.path import join
from PyQt6 import QtCore, QtGui, QtWidgets


class ConnectToServerWindowDesign(object):
    def setupUi(self, MainWindow, language: str="en"):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(901, 579)
        MainWindow.setStyleSheet("background-color: rgb(64, 65, 62);\n"
"color: black;")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 411, 361))
        self.frame.setStyleSheet("background-color: rgb(35, 35, 35);\n"
"border-radius: 15px;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.ip = QtWidgets.QLineEdit(parent=self.frame)
        self.ip.setGeometry(QtCore.QRect(10, 10, 391, 61))
        self.ip.setStyleSheet("background-color: rgb(229, 229, 229);\n"
"border-radius: 15px;\n"
"padding-left: 5px;\n"
"font-size: 15px")
        self.ip.setObjectName("ip")
        self.connect_to_server = QtWidgets.QPushButton(parent=self.frame)
        self.connect_to_server.setGeometry(QtCore.QRect(10, 290, 391, 61))
        self.connect_to_server.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.connect_to_server.setStyleSheet("QPushButton {\n"
"    background-color: rgb(123, 123, 123);\n"
"    border-radius: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(108, 108, 108);\n"
"}")
        self.connect_to_server.setObjectName("connect_to_server")
        self.nikname = QtWidgets.QLineEdit(parent=self.frame)
        self.nikname.setGeometry(QtCore.QRect(10, 150, 391, 61))
        self.nikname.setStyleSheet("background-color: rgb(229, 229, 229);\n"
"border-radius: 15px;\n"
"padding-left: 5px;\n"
"font-size: 15px")
        self.nikname.setObjectName("nikname")
        self.port = QtWidgets.QLineEdit(parent=self.frame)
        self.port.setGeometry(QtCore.QRect(10, 80, 391, 61))
        self.port.setStyleSheet("background-color: rgb(229, 229, 229);\n"
"border-radius: 15px;\n"
"padding-left: 5px;\n"
"font-size: 15px")
        self.port.setObjectName("port")
        self.save = QtWidgets.QPushButton(parent=self.frame)
        self.save.setGeometry(QtCore.QRect(10, 220, 391, 61))
        self.save.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.save.setStyleSheet("QPushButton {\n"
"    background-color: rgb(123, 123, 123);\n"
"    border-radius: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(108, 108, 108);\n"
"}")
        self.save.setObjectName("save")
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(430, 10, 461, 361))
        self.frame_2.setStyleSheet("background-color: rgb(35, 35, 35);\n"
"border-radius: 15px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.servers = QtWidgets.QTableWidget(parent=self.frame_2)
        self.servers.setGeometry(QtCore.QRect(10, 10, 441, 201))
        self.servers.setStyleSheet("background-color: rgb(184, 184, 184);\n"
"border-radius: 15px;")
        self.servers.setObjectName("servers")
        self.servers.setColumnCount(0)
        self.servers.setRowCount(0)
        self.add_server = QtWidgets.QPushButton(parent=self.frame_2)
        self.add_server.setGeometry(QtCore.QRect(10, 220, 211, 61))
        self.add_server.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.add_server.setStyleSheet("QPushButton {\n"
"    background-color: rgb(123, 123, 123);\n"
"    border-radius: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(108, 108, 108);\n"
"}")
        self.add_server.setObjectName("add_server")
        self.delete_server = QtWidgets.QPushButton(parent=self.frame_2)
        self.delete_server.setGeometry(QtCore.QRect(240, 220, 211, 61))
        self.delete_server.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.delete_server.setStyleSheet("QPushButton {\n"
"    background-color: rgb(123, 123, 123);\n"
"    border-radius: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(108, 108, 108);\n"
"}")
        self.delete_server.setObjectName("delete_server")
        self.apply_server = QtWidgets.QPushButton(parent=self.frame_2)
        self.apply_server.setGeometry(QtCore.QRect(10, 290, 441, 61))
        self.apply_server.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.apply_server.setStyleSheet("QPushButton {\n"
"    background-color: rgb(123, 123, 123);\n"
"    border-radius: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(108, 108, 108);\n"
"}")
        self.apply_server.setObjectName("apply_server")
        self.frame_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(10, 380, 881, 191))
        self.frame_3.setStyleSheet("background-color: rgb(35, 35, 35);\n"
"border-radius: 15px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.language_label = QtWidgets.QLabel(parent=self.frame_3)
        self.language_label.setGeometry(QtCore.QRect(10, 0, 861, 41))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        self.language_label.setFont(font)
        self.language_label.setStyleSheet("color: white;")
        self.language_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.language_label.setObjectName("language_label")
        self.new_language = QtWidgets.QComboBox(parent=self.frame_3)
        self.new_language.setGeometry(QtCore.QRect(300, 60, 141, 91))
        self.new_language.setStyleSheet("background-color: none;\n"
"color: white;")
        self.new_language.setObjectName("new_language")
        self.new_language.addItem("")
        self.new_language.addItem("")
        self.set_language = QtWidgets.QPushButton(parent=self.frame_3)
        self.set_language.setGeometry(QtCore.QRect(450, 60, 151, 91))
        self.set_language.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.set_language.setStyleSheet("QPushButton {\n"
"    background-color: rgb(123, 123, 123);\n"
"    border-radius: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(108, 108, 108);\n"
"}")
        self.set_language.setObjectName("set_language")
        self.translations_note = QtWidgets.QLabel(parent=self.frame_3)
        self.translations_note.setGeometry(QtCore.QRect(10, 160, 861, 20))
        self.translations_note.setStyleSheet("color: white;")
        self.translations_note.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.translations_note.setObjectName("translations_note")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow, language)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow, language):
        self.language = language

        with open(join("design", "translation.json"), "r", encoding="utf-8") as translation_file:
            translation = load(translation_file)[language]

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", translation["connect_to_server_window_title"]))
        self.ip.setPlaceholderText(_translate("MainWindow", translation["ip"]))
        self.connect_to_server.setText(_translate("MainWindow", translation["connect"]))
        self.nikname.setPlaceholderText(_translate("MainWindow", translation["ip"]))
        self.port.setPlaceholderText(_translate("MainWindow", translation["port"]))
        self.save.setText(_translate("MainWindow", translation["save"]))
        self.add_server.setText(_translate("MainWindow", translation["add_server"]))
        self.delete_server.setText(_translate("MainWindow", translation["delete_server"]))
        self.apply_server.setText(_translate("MainWindow", translation["apply"]))
        self.language_label.setText(_translate("MainWindow", translation["language_label"]))
        self.new_language.setItemText(0, _translate("MainWindow", "Українська"))
        self.new_language.setItemText(1, _translate("MainWindow", "English"))
        self.set_language.setText(_translate("MainWindow", translation["set_language"]))
        self.translations_note.setText(_translate("MainWindow", translation["translations_note"]))
