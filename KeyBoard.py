# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'KeyBoard.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Keyboar(object):
    def setupUi(self, Keyboar):
        Keyboar.setObjectName("Keyboar")
        Keyboar.resize(361, 204)
        Keyboar.setMinimumSize(QtCore.QSize(361, 204))
        Keyboar.setMaximumSize(QtCore.QSize(361, 204))
        self.pushButton = QtWidgets.QPushButton(Keyboar)
        self.pushButton.setGeometry(QtCore.QRect(60, 150, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(252, 86, 50);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Keyboar)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 150, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgba(0, 170, 0, 180);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Keyboar)
        self.label.setGeometry(QtCore.QRect(50, 20, 61, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(Keyboar)
        self.textBrowser.setGeometry(QtCore.QRect(50, 50, 261, 81))
        self.textBrowser.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Keyboar)
        QtCore.QMetaObject.connectSlotsByName(Keyboar)

    def retranslateUi(self, Keyboar):
        _translate = QtCore.QCoreApplication.translate
        Keyboar.setWindowTitle(_translate("Keyboar", "按键测试"))
        self.pushButton.setText(_translate("Keyboar", "失败"))
        self.pushButton_2.setText(_translate("Keyboar", "通过"))
        self.label.setText(_translate("Keyboar", "请按按键："))