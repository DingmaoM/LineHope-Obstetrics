# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Sensor.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Sensor(object):
    def setupUi(self, Sensor):
        Sensor.setObjectName("Sensor")
        Sensor.resize(399, 318)
        Sensor.setMinimumSize(QtCore.QSize(399, 318))
        Sensor.setMaximumSize(QtCore.QSize(399, 318))
        self.label = QtWidgets.QLabel(Sensor)
        self.label.setGeometry(QtCore.QRect(40, 100, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Sensor)
        self.label_2.setGeometry(QtCore.QRect(210, 100, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Sensor)
        self.label_3.setGeometry(QtCore.QRect(40, 140, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Sensor)
        self.label_4.setGeometry(QtCore.QRect(210, 140, 91, 20))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Sensor)
        self.label_5.setGeometry(QtCore.QRect(60, 180, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Sensor)
        self.label_6.setGeometry(QtCore.QRect(240, 180, 61, 20))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Sensor)
        self.label_7.setGeometry(QtCore.QRect(90, 220, 31, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.OpenSensor = QtWidgets.QLabel(Sensor)
        self.OpenSensor.setGeometry(QtCore.QRect(130, 100, 53, 15))
        font = QtGui.QFont()
        font.setBold(True)
        self.OpenSensor.setFont(font)
        self.OpenSensor.setText("")
        self.OpenSensor.setObjectName("OpenSensor")
        self.CloseSensor = QtWidgets.QLabel(Sensor)
        self.CloseSensor.setGeometry(QtCore.QRect(310, 100, 53, 15))
        font = QtGui.QFont()
        font.setBold(True)
        self.CloseSensor.setFont(font)
        self.CloseSensor.setText("")
        self.CloseSensor.setObjectName("CloseSensor")
        self.ResetSensor = QtWidgets.QLabel(Sensor)
        self.ResetSensor.setGeometry(QtCore.QRect(130, 140, 53, 15))
        font = QtGui.QFont()
        font.setBold(True)
        self.ResetSensor.setFont(font)
        self.ResetSensor.setText("")
        self.ResetSensor.setObjectName("ResetSensor")
        self.fangqiao = QtWidgets.QLabel(Sensor)
        self.fangqiao.setGeometry(QtCore.QRect(310, 140, 53, 15))
        font = QtGui.QFont()
        font.setBold(True)
        self.fangqiao.setFont(font)
        self.fangqiao.setText("")
        self.fangqiao.setObjectName("fangqiao")
        self.chonzhi = QtWidgets.QLabel(Sensor)
        self.chonzhi.setGeometry(QtCore.QRect(130, 180, 53, 15))
        font = QtGui.QFont()
        font.setBold(True)
        self.chonzhi.setFont(font)
        self.chonzhi.setText("")
        self.chonzhi.setObjectName("chonzhi")
        self.peiwang = QtWidgets.QLabel(Sensor)
        self.peiwang.setGeometry(QtCore.QRect(310, 180, 53, 15))
        font = QtGui.QFont()
        font.setBold(True)
        self.peiwang.setFont(font)
        self.peiwang.setText("")
        self.peiwang.setObjectName("peiwang")
        self.menci = QtWidgets.QLabel(Sensor)
        self.menci.setGeometry(QtCore.QRect(130, 220, 53, 15))
        font = QtGui.QFont()
        font.setBold(True)
        self.menci.setFont(font)
        self.menci.setText("")
        self.menci.setObjectName("menci")
        self.pushButton = QtWidgets.QPushButton(Sensor)
        self.pushButton.setGeometry(QtCore.QRect(90, 260, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(252, 86, 50);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Sensor)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 260, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgba(0, 170, 0, 180);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Sensor)
        self.textBrowser_2.setGeometry(QtCore.QRect(30, 20, 341, 61))
        self.textBrowser_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.retranslateUi(Sensor)
        QtCore.QMetaObject.connectSlotsByName(Sensor)

    def retranslateUi(self, Sensor):
        _translate = QtCore.QCoreApplication.translate
        Sensor.setWindowTitle(_translate("Sensor", "Sensor开关测试"))
        self.label.setText(_translate("Sensor", "OpenSensor："))
        self.label_2.setText(_translate("Sensor", "CloseSensor："))
        self.label_3.setText(_translate("Sensor", "ResetSensor："))
        self.label_4.setText(_translate("Sensor", "防撬："))
        self.label_5.setText(_translate("Sensor", "重置按键："))
        self.label_6.setText(_translate("Sensor", "配网按键："))
        self.label_7.setText(_translate("Sensor", "门磁："))
        self.pushButton.setText(_translate("Sensor", "失败"))
        self.pushButton_2.setText(_translate("Sensor", "通过"))
        self.textBrowser_2.setHtml(_translate("Sensor", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Microsoft YaHei UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">请改变开关或按键状态，查看开关或按键是否正常改变状态</span></p></body></html>"))
