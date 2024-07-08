# Form implementation generated from reading ui file 'design/QtDesigner/main_window.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class MainWindowDesign(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1190, 639)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet("background-color: rgb(64, 65, 62); color: black;")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.messages = QtWidgets.QListWidget(parent=self.centralwidget)
        self.messages.setGeometry(QtCore.QRect(440, 20, 731, 391))
        self.messages.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.messages.setStyleSheet("background-color: rgb(183, 183, 183);\n"
"border-radius: 15px;")
        self.messages.setObjectName("messages")
        self.send_message = QtWidgets.QPushButton(parent=self.centralwidget)
        self.send_message.setGeometry(QtCore.QRect(440, 490, 361, 61))
        self.send_message.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.send_message.setStyleSheet("QPushButton {\n"
"    background-color: rgb(123, 123, 123);\n"
"    border-radius: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(108, 108, 108);\n"
"}")
        self.send_message.setObjectName("send_message")
        self.connect_to_server = QtWidgets.QPushButton(parent=self.centralwidget)
        self.connect_to_server.setGeometry(QtCore.QRect(440, 560, 731, 61))
        self.connect_to_server.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.connect_to_server.setStyleSheet("QPushButton {\n"
"    background-color: rgb(123, 123, 123);\n"
"    border-radius: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(108, 108, 108);\n"
"}")
        self.connect_to_server.setObjectName("connect_to_server")
        self.exit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(810, 490, 361, 61))
        self.exit.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.exit.setStyleSheet("QPushButton {\n"
"    background-color: rgb(123, 123, 123);\n"
"    border-radius: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(108, 108, 108);\n"
"}")
        self.exit.setObjectName("exit")
        self.message = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.message.setGeometry(QtCore.QRect(440, 420, 731, 61))
        self.message.setStyleSheet("background-color: rgb(229, 229, 229);\n"
"border-radius: 15px;\n"
"padding-left: 5px;\n"
"font-size: 15px")
        self.message.setObjectName("message")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 411, 621))
        self.frame.setStyleSheet("background-color: rgb(35, 35, 35);\n"
"border-radius: 15px;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 391, 51))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.sticker1 = QtWidgets.QPushButton(parent=self.frame)
        self.sticker1.setGeometry(QtCore.QRect(20, 70, 111, 111))
        self.sticker1.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.sticker1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("design/QtDesigner/../../assets/1.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.sticker1.setIcon(icon)
        self.sticker1.setIconSize(QtCore.QSize(100, 100))
        self.sticker1.setCheckable(False)
        self.sticker1.setAutoRepeat(False)
        self.sticker1.setAutoExclusive(False)
        self.sticker1.setAutoDefault(False)
        self.sticker1.setDefault(False)
        self.sticker1.setFlat(False)
        self.sticker1.setObjectName("sticker1")
        self.sticker2 = QtWidgets.QPushButton(parent=self.frame)
        self.sticker2.setGeometry(QtCore.QRect(150, 70, 111, 111))
        self.sticker2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.sticker2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("design/QtDesigner/../../assets/2.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.sticker2.setIcon(icon1)
        self.sticker2.setIconSize(QtCore.QSize(100, 100))
        self.sticker2.setCheckable(False)
        self.sticker2.setAutoRepeat(False)
        self.sticker2.setAutoExclusive(False)
        self.sticker2.setAutoDefault(False)
        self.sticker2.setDefault(False)
        self.sticker2.setFlat(False)
        self.sticker2.setObjectName("sticker2")
        self.sticker3 = QtWidgets.QPushButton(parent=self.frame)
        self.sticker3.setGeometry(QtCore.QRect(280, 70, 111, 111))
        self.sticker3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.sticker3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("design/QtDesigner/../../assets/3.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.sticker3.setIcon(icon2)
        self.sticker3.setIconSize(QtCore.QSize(100, 100))
        self.sticker3.setCheckable(False)
        self.sticker3.setAutoRepeat(False)
        self.sticker3.setAutoExclusive(False)
        self.sticker3.setAutoDefault(False)
        self.sticker3.setDefault(False)
        self.sticker3.setFlat(False)
        self.sticker3.setObjectName("sticker3")
        self.sticker5 = QtWidgets.QPushButton(parent=self.frame)
        self.sticker5.setGeometry(QtCore.QRect(150, 190, 111, 111))
        self.sticker5.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.sticker5.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("design/QtDesigner/../../assets/5.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.sticker5.setIcon(icon3)
        self.sticker5.setIconSize(QtCore.QSize(100, 100))
        self.sticker5.setCheckable(False)
        self.sticker5.setAutoRepeat(False)
        self.sticker5.setAutoExclusive(False)
        self.sticker5.setAutoDefault(False)
        self.sticker5.setDefault(False)
        self.sticker5.setFlat(False)
        self.sticker5.setObjectName("sticker5")
        self.sticker6 = QtWidgets.QPushButton(parent=self.frame)
        self.sticker6.setGeometry(QtCore.QRect(280, 190, 111, 111))
        self.sticker6.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.sticker6.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("design/QtDesigner/../../assets/6.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.sticker6.setIcon(icon4)
        self.sticker6.setIconSize(QtCore.QSize(100, 100))
        self.sticker6.setCheckable(False)
        self.sticker6.setAutoRepeat(False)
        self.sticker6.setAutoExclusive(False)
        self.sticker6.setAutoDefault(False)
        self.sticker6.setDefault(False)
        self.sticker6.setFlat(False)
        self.sticker6.setObjectName("sticker6")
        self.sticker4 = QtWidgets.QPushButton(parent=self.frame)
        self.sticker4.setGeometry(QtCore.QRect(20, 190, 111, 111))
        self.sticker4.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.sticker4.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("design/QtDesigner/../../assets/4.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.sticker4.setIcon(icon5)
        self.sticker4.setIconSize(QtCore.QSize(100, 100))
        self.sticker4.setCheckable(False)
        self.sticker4.setAutoRepeat(False)
        self.sticker4.setAutoExclusive(False)
        self.sticker4.setAutoDefault(False)
        self.sticker4.setDefault(False)
        self.sticker4.setFlat(False)
        self.sticker4.setObjectName("sticker4")
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(430, 10, 751, 621))
        self.frame_2.setStyleSheet("background-color: rgb(35, 35, 35);\n"
"border-radius: 15px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.raise_()
        self.messages.raise_()
        self.send_message.raise_()
        self.connect_to_server.raise_()
        self.exit.raise_()
        self.message.raise_()
        self.frame.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AChat"))
        self.send_message.setText(_translate("MainWindow", "Відправити"))
        self.connect_to_server.setText(_translate("MainWindow", "Підключитися"))
        self.exit.setText(_translate("MainWindow", "Вийти"))
        self.message.setPlaceholderText(_translate("MainWindow", "Введіть повідомлення"))
        self.label.setText(_translate("MainWindow", "Стікери"))
