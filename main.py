import configparser
import os.path
import re
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QAbstractItemView, QTableWidgetItem, QDialog, QMessageBox
from Login import Ui_Login
from Home import Ui_Home
from correspond import Cor
from Message import Ui_Message
from KeyBoard import Ui_Keyboar
from Sensor import Ui_Sensor
import time
import threading
import sys
import pandas as pd


class Login(Ui_Login):

    LOCK_CODE = 0

    def __init__(self):
        super(Login, self).__init__()
        self.ui = QMainWindow()
        self.setupUi(self.ui)
        self.ui.show()
        self.pushButton.clicked.connect(self.stat_testing)  # 点击登录事件
        self.checkBox_14.clicked.connect(self.test_item_click_01)
        self.checkBox_13.clicked.connect(self.test_item_click_01)
        self.checkBox_12.clicked.connect(self.test_item_click_01)
        self.checkBox_11.clicked.connect(self.test_item_click_01)
        self.checkBox_10.clicked.connect(self.test_item_click)
        self.checkBox_9.clicked.connect(self.test_item_click_01)
        self.checkBox_8.clicked.connect(self.test_item_click_01)
        self.checkBox_7.clicked.connect(self.test_item_click_01)
        self.checkBox_6.clicked.connect(self.test_item_click_01)
        self.checkBox_5.clicked.connect(self.test_item_click_01)
        self.checkBox_4.clicked.connect(self.test_item_click_01)
        self.checkBox_3.clicked.connect(self.test_item_click_01)
        self.checkBox_2.clicked.connect(self.test_item_click_01)
        self.checkBox.clicked.connect(self.test_item_click_01)
        self.comboBox.activated[int].connect(self.product_selection)
        self.lineEdit_2.setText(self.get_num("code", "min"))
        self.lineEdit_3.setText(self.get_num("code", "max"))
        self.lineEdit.setText(self.get_num("version", "s2"))


    @staticmethod
    def get_current_time():
        ct = time.time()
        local_time = time.localtime(ct)
        data_head = time.strftime("%Y-%m-%d %H:%M", local_time)
        return data_head

    # 从config.ini文件获取序列号最小值
    def get_num(self, name1, name2):
        cf = configparser.ConfigParser()
        filename = "config.ini"
        cf.read(filename)
        data = cf.get(name1, name2)
        return data

    def get_Testing_item(self):
        test_item = []

        if self.checkBox.checkState() == 2:
            test_item.append(self.checkBox.text())
        if self.checkBox_2.checkState() == 2:
            test_item.append(self.checkBox_2.text())
        if self.checkBox_4.checkState() == 2:
            test_item.append(self.checkBox_4.text())

        if self.comboBox.currentIndex() == 0:
            if self.checkBox_13.checkState() == 2:
                test_item.append(self.checkBox_13.text())
            if self.checkBox_14.checkState() == 2:
                test_item.append(self.checkBox_14.text())
        elif self.comboBox.currentIndex() == 2:
            if self.checkBox_13.checkState() == 2:
                test_item.append(self.checkBox_13.text())
            if self.checkBox_14.checkState() == 2:
                test_item.append(self.checkBox_14.text())

        if self.checkBox_5.checkState() == 2:
            test_item.append(self.checkBox_5.text())
        if self.checkBox_7.checkState() == 2:
            test_item.append(self.checkBox_7.text())
        if self.checkBox_8.checkState() == 2:
            test_item.append(self.checkBox_8.text())
        if self.checkBox_11.checkState() == 2:
            test_item.append(self.checkBox_11.text())
        if self.checkBox_9.checkState() == 2:
            test_item.append(self.checkBox_9.text())
        if self.checkBox_12.checkState() == 2:
            test_item.append(self.checkBox_12.text())
        if self.checkBox_3.checkState() == 2:
            test_item.append(self.checkBox_3.text())
        if self.checkBox_6.checkState() == 2:
            test_item.append(self.checkBox_6.text())
        return test_item

    test_item = ["序号", "结果", "版本号", "电量", "MCU引脚", "序列号"]

    # 开始测试按钮事件
    def stat_testing(self):
        for i in self.get_Testing_item():
            self.test_item.append(i)
        self.test_item.append("耗时")
        home.tableWidget.setColumnCount(len(self.test_item))
        home.tableWidget.setRowCount(1)
        home.tableWidget.setHorizontalHeaderLabels(self.test_item)
        home.home_ui.show()
        self.ui.close()

        ct = time.time()
        local_time = time.localtime(ct)
        data_head = time.strftime("%Y%m%d", local_time)
        product_name = self.comboBox.currentText()
        if os.path.exists('./log'):
            pass
        else:
            os.mkdir('./log')
        file_name = './log/{}{}.xlsx'.format(data_head, product_name)
        if os.path.isfile(file_name):
            pass
        else:
            if product_name == "玻璃门锁C1S":
                data = [['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']]
                df = pd.DataFrame(data,
                                  columns=['序号', '结果', '版本号', '电量', 'MCU引脚', '序列号', '电机测试', '指纹录入', '指纹RGB',
                                           '喇叭测试', '键盘背光', '按键触摸', 'RTC测试', 'Flash测试', 'Sensor测试',
                                           '设备初始化', '功耗测试', '耗时', '日期', '序列号'])
                df.to_excel(file_name, index=False)
            else:
                data = [['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']]
                df = pd.DataFrame(data,
                                  columns=['序号', '结果', '版本号', '电量', 'MCU引脚', '序列号', '电机测试', '指纹录入', '指纹RGB',
                                           '门卡测试', '呼吸灯测试', '喇叭测试', '键盘背光', '按键触摸', 'RTC测试',
                                           'Flash测试', 'Sensor测试', '设备初始化', '功耗测试', '耗时', '日期', '序列号'])
                df.to_excel(file_name, index=False)
        home.set_num("code", "max", self.lineEdit_3.text())

    # 全选按钮事件
    def test_item_click(self):
        if self.checkBox_10.checkState() == 0:
            self.checkBox_14.setChecked(False)
            self.checkBox_13.setChecked(False)
            self.checkBox_12.setChecked(False)
            self.checkBox_11.setChecked(False)
            self.checkBox_9.setChecked(False)
            self.checkBox_8.setChecked(False)
            self.checkBox_7.setChecked(False)
            self.checkBox_6.setChecked(False)
            self.checkBox_5.setChecked(False)
            self.checkBox_4.setChecked(False)
            self.checkBox_3.setChecked(False)
            self.checkBox_2.setChecked(False)
            self.checkBox.setChecked(False)
        else:
            self.checkBox_14.setChecked(True)
            self.checkBox_13.setChecked(True)
            self.checkBox_12.setChecked(True)
            self.checkBox_11.setChecked(True)
            self.checkBox_9.setChecked(True)
            self.checkBox_8.setChecked(True)
            self.checkBox_7.setChecked(True)
            self.checkBox_6.setChecked(True)
            self.checkBox_5.setChecked(True)
            self.checkBox_4.setChecked(True)
            self.checkBox_3.setChecked(True)
            self.checkBox_2.setChecked(True)
            self.checkBox.setChecked(True)

    # 测试项取消全选事件
    def test_item_click_01(self):
        if self.checkBox.checkState() == 0:
            if self.checkBox_9.checkState() == 2 and self.checkBox_8.checkState() == 2 and self.checkBox_7.checkState() == 2\
                    and self.checkBox_6.checkState() == 2 and self.checkBox_5.checkState() == 2 and\
                    self.checkBox_4.checkState() == 2 and self.checkBox_3.checkState() == 2 and\
                    self.checkBox_2.checkState() == 2 and self.checkBox.checkState() == 2 and \
                    self.checkBox_11.checkState() == 2 and self.checkBox_12.checkState() == 2\
                    and self.checkBox_13.checkState() == 2 and self.checkBox_14.checkState() == 2:
                self.checkBox_10.setChecked(True)
            elif self.checkBox_9.checkState() == 0 or self.checkBox_8.checkState() == 0 or self.checkBox_7.checkState() == 0\
                    or self.checkBox_6.checkState() == 0 or self.checkBox_5.checkState() == 0\
                    or self.checkBox_4.checkState() == 0 or self.checkBox_3.checkState() == 0\
                    or self.checkBox_2.checkState() == 0 or self.checkBox.checkState() == 0\
                    or self.checkBox_11.checkState() == 0 or self.checkBox_12.checkState() == 0\
                    or self.checkBox_13.checkState() == 0 or self.checkBox_14.checkState() == 0:
                self.checkBox_10.setChecked(False)
        elif self.checkBox.checkState() == 2:
            if self.checkBox_9.checkState() == 2 and self.checkBox_8.checkState() == 2 and self.checkBox_7.checkState() == 2 \
                    and self.checkBox_6.checkState() == 2 and self.checkBox_5.checkState() == 2 and \
                    self.checkBox_4.checkState() == 2 and self.checkBox_3.checkState() == 2 and \
                    self.checkBox_2.checkState() == 2 and self.checkBox.checkState() == 2 and \
                    self.checkBox_11.checkState() == 2 and self.checkBox_12.checkState() == 2 \
                    and self.checkBox_13.checkState() == 2 and self.checkBox_14.checkState() == 2:
                self.checkBox_10.setChecked(True)
            elif self.checkBox_9.checkState() == 0 or self.checkBox_8.checkState() == 0 or self.checkBox_7.checkState() == 0 \
                    or self.checkBox_6.checkState() == 0 or self.checkBox_5.checkState() == 0 \
                    or self.checkBox_4.checkState() == 0 or self.checkBox_3.checkState() == 0 \
                    or self.checkBox_2.checkState() == 0 or self.checkBox.checkState() == 0 \
                    or self.checkBox_11.checkState() == 0 or self.checkBox_12.checkState() == 0 \
                    or self.checkBox_13.checkState() == 0 or self.checkBox_14.checkState() == 0:
                self.checkBox_10.setChecked(False)

    # 产品选择事件
    def product_selection(self, d):
        if d == 1:
            self.checkBox_13.hide()  # 隐藏卡片测试
            self.checkBox_14.hide()  # 隐藏呼吸灯测试
            self.lineEdit.setText(self.get_num("version", "c1s"))
        elif d == 0:
            self.checkBox_13.show()
            self.checkBox_14.show()
            self.lineEdit.setText(self.get_num("version", "s2"))
        elif d == 2:
            self.checkBox_13.show()
            self.checkBox_14.show()
            self.lineEdit.setText(self.get_num("version", "as2"))


class Message_Page(Ui_Message):

    STATE = 0

    def __init__(self):
        super(Message_Page, self).__init__()
        self.mes = QDialog()
        self.setupUi(self.mes)
        self.pushButton.clicked.connect(self.f)
        self.pushButton_2.clicked.connect(self.succ)
        # self.mes.setWindowFlags(Qt.WindowContextHelpButtonHint | Qt.WindowCloseButtonHint)
        # self.mes.setWindowFlags(self.windowFlags() & Qt.WindowContextHelpButtonHint)
        self.mes.setWindowFlag(Qt.FramelessWindowHint)  # 设置窗体无标题栏
        # self.mes.setWindowOpacity(1)  # 设置窗体透明

    def showDialog(self):
        self.mes.setWindowModality(Qt.ApplicationModal)
        self.mes.exec()

    def f(self):
        self.STATE = 1
        self.mes.close()

    def succ(self):
        self.STATE = 0
        self.mes.close()


class KeyBoard_Page(Ui_Keyboar):

    STATE = 0

    def __init__(self):
        super(KeyBoard_Page, self).__init__()
        self.key = QDialog()
        self.setupUi(self.key)
        self.pushButton.clicked.connect(self.fail)
        self.pushButton_2.clicked.connect(self.su)

    def showDialog(self):
        self.key.setWindowModality(Qt.ApplicationModal)
        self.key.exec()

    def fail(self):
        self.STATE = 1
        self.key.close()

    def su(self):
        self.STATE = 0
        self.key.close()


class Sensor_Page(Ui_Sensor):

    STATE = 0

    def __init__(self):
        super(Sensor_Page, self).__init__()
        self.sen = QDialog()
        self.setupUi(self.sen)
        self.pushButton.clicked.connect(self.f)
        self.pushButton_2.clicked.connect(self.succ)

    def showDialog(self):
        self.sen.setWindowModality(Qt.ApplicationModal)
        self.sen.exec()

    def f(self):
        self.STATE = 1
        self.sen.close()

    def succ(self):
        self.STATE = 0
        self.sen.close()


class Home_Page(Ui_Home):

    RESULT = 0
    RESULT_01 = 0
    RESULT_02 = 0
    RESULT_03 = 0
    RESULT_04 = 0
    RESULT_05 = 0
    RESULT_06 = 0
    RESULT_07 = 0
    RESULT_08 = 0
    RESULT_09 = 0
    RESULT_10 = 0
    RESULT_11 = 0
    RESULT_12 = 0
    RESULT_13 = 0
    RESULT_14 = 0
    RESULT_15 = 0
    key_code = 0  # 测试设备序号
    COL_CODE = 5  # 当前列数
    TOTAL = 0  # 测试总数
    SUCCESS = 0  # 测试成功数
    FAIL = 0  # 测试失败数
    TESTING_BUT = 0  # 测试状态，测试过程中会先判断是否为0,0则继续下一次测试，1则退出测试



    def __init__(self):
        super(Home_Page, self).__init__()
        self.home_ui = QMainWindow()
        self.setupUi(self.home_ui)

        self.label.setText(win.get_current_time())  # 显示测试开始测试时间
        font = self.tableWidget.horizontalHeader().font()
        font.setBold(True)
        self.tableWidget.horizontalHeader().setFont(font)  # 设置表头字体加粗
        self.tableWidget.setFont(QFont('Times', 10))  # 设置全局字体
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 设置表格不可编辑
        self.tableWidget.horizontalHeader().setMinimumHeight(40)  # 设置表头高度
        self.tableWidget.setRowHeight(0, 40)  # 设置测试页表格行高
        self.pushButton_2.clicked.connect(self.back_click)  # 返回首页按钮事件绑定
        self.pushButton.clicked.connect(self.run)  # 开始测试按钮事件绑定
        self.pushButton_3.clicked.connect(self.refresh_port_list)
        self.comboBox.addItems(cor.get_port_01())  # 获取端口列表显示到comboBox下拉列表

    # 测试失败插入表中数据
    def fail_font(self):
        fail = QTableWidgetItem("×")
        fail.setFont(QFont('微软雅黑', 18, QFont.Black))
        fail.setTextAlignment(Qt.AlignCenter)
        fail.setForeground(QBrush(QColor(252, 86, 50)))
        return fail

    # 测试成功插入表中数据
    def success_font(self):
        success = QTableWidgetItem("√")
        success.setFont(QFont('微软雅黑', 18, QFont.Black))
        success.setTextAlignment(Qt.AlignCenter)
        success.setForeground(QBrush(QColor(0, 170, 0)))
        return success

    # 设置序列号最小值到config.ini文件中
    def set_num(self, node, name, data):
        cf = configparser.ConfigParser()
        filename = "config.ini"
        cf.read(filename)
        cf.set(node, name, data)
        fh = open(filename, 'w')
        cf.write(fh)
        fh.close()


    # 刷新端口号列表
    def refresh_port_list(self):
        self.comboBox.clear()
        self.comboBox.addItems(cor.get_port_01())

    # 返回首页按钮事件
    def back_click(self):
        self.home_ui.close()
        self.tableWidget.clear()
        self.key_code = 0
        win.test_item = ["序号", "结果", "版本号", "电量", "MCU引脚", "序列号"]
        win.ui.show()

    # 往表中插入数据
    def tabel_itme_insert(self, data):
        item = QTableWidgetItem(data)
        item.setTextAlignment(Qt.AlignCenter)
        return item

    # 获取当前时间年月给写入SN码使用
    def get_SN_Time(self):
        ct = time.time()
        local_time = time.localtime(ct)
        data_head = time.strftime("%Y%m", local_time)
        return data_head[2:]

    # 获取当前时间给插入日志方法使用
    def get_log_time(self):
        ct = time.time()
        local_time = time.localtime(ct)
        data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
        return data_head + ":" + "   "

    # 获取选择的端口字符串，使用正则剥离出端口号，返回给发送协议使用
    def port(self):
        port_list = self.comboBox.currentText()
        port = re.findall(r'COM\d+', port_list)
        return port[0]

    # 在日志内容框中插入传入的内容
    def upatat_log(self, log):
        self.textEdit.append(self.get_log_time() + log)
        QApplication.processEvents()

    # 按键测试将获得十进制转成对应的按键
    def key_upatat(self, log):
        data = []
        num = log[1:]
        if num == "b":
            data.append("*")
        elif num == "c":
            data.append("#")
        elif num == "d":
            data.append("门铃")
        elif num == "e":
            data.append("静音")
        else:
            data.append(num)
        key.textBrowser.append("  ".join(data))
        key.textBrowser.moveCursor(key.textBrowser.textCursor().End)
        QApplication.processEvents()

    def sensor_updata(self, sensor_code):
        if win.comboBox.currentIndex() == 1:
            if sensor_code[:2] == "00":
                sens.OpenSensor.setText("关")
            elif sensor_code[:2] == "01":
                sens.OpenSensor.setText("开")
            if sensor_code[2:4] == "00":
                sens.CloseSensor.setText("关")
            elif sensor_code[2:4] == "01":
                sens.CloseSensor.setText("开")
            if sensor_code[4:6] == "00":
                sens.ResetSensor.setText("关")
            elif sensor_code[4:6] == "01":
                sens.ResetSensor.setText("开")
            if sensor_code[6:8] == "00":
                sens.fangqiao.setText("压住")
            elif sensor_code[6:8] == "01":
                sens.fangqiao.setText("弹开")
            if sensor_code[10:12] == "00":
                sens.chonzhi.setText("压住")
            elif sensor_code[10:12] == "01":
                sens.chonzhi.setText("弹出")
            if sensor_code[12:14] == "00":
                sens.peiwang.setText("压住")
            elif sensor_code[12:14] == "01":
                sens.peiwang.setText("弹开")
            if sensor_code[14:16] == "00":
                sens.menci.setText("靠近")
            elif sensor_code[14:16] == "01":
                sens.menci.setText("移开")
        elif win.comboBox.currentIndex() == 0 or 2:
            if sensor_code[:2] == "00":
                sens.OpenSensor.setText("压住")
            elif sensor_code[:2] == "01":
                sens.OpenSensor.setText("弹出")
            if sensor_code[2:4] == "00":
                sens.CloseSensor.setText("压住")
            elif sensor_code[2:4] == "01":
                sens.CloseSensor.setText("弹出")
            if sensor_code[4:6] == "00":
                sens.ResetSensor.setText("压住")
            elif sensor_code[4:6] == "01":
                sens.ResetSensor.setText("弹出")
            if sensor_code[6:8] == "00":
                sens.fangqiao.setText("正常")
            elif sensor_code[6:8] == "01":
                sens.fangqiao.setText("异常")
        QApplication.processEvents()

    key_state = True

    def keyboard(self):
        keyboard_code = "43 4D 44 76 00 76"
        code = cor.send_data(keyboard_code, 0.5, self.port())
        if code == 0:
            self.upatat_log("返回码为空！")
            self.TESTING_BUT = 1
        elif code == 1:
            self.upatat_log("端口异常！")
            self.TESTING_BUT = 1
        else:
            if code[-4:-2] == "00":
                while self.key_state is True:
                    keyboard = cor.receive(0.1, self.port())
                    if keyboard is None:
                        pass
                    else:
                        self.key_upatat(keyboard[-4:-2])
            elif code[-4:-2] == "01":
                self.upatat_log("键盘激活失败！")
                self.tableWidget.setItem(self.key_code, 14, self.fail_font())

    sensor_state = True

    # 循环获取sensor开关状态
    def sensor_while(self):
        while self.sensor_state is True:
            key_code = cor.receive(0.1, self.port())
            if key_code is None:
                pass
            else:
                self.sensor_updata(key_code[10:-2])

    def version_01(self):
        self.upatat_log("开始验证固件版本号！")
        version_data = win.lineEdit.text()
        version_1 = cor.version(self.port())
        if version_1 == 0:
            self.upatat_log("返回码为空！")
            self.TESTING_BUT = 1
        elif version_1 == 1:
            self.upatat_log("端口异常！")
            self.TESTING_BUT = 1
        else:
            if version_1 == version_data:
                self.tableWidget.setItem(self.key_code, 2, self.success_font())
                self.upatat_log("版本号测试完成。" + version_1)
                self.RESULT = 0
            else:
                self.upatat_log("版本号错误。" + version_1)
                self.tableWidget.setItem(self.key_code, 2, self.fail_font())
                self.RESULT = 1

    def electricity_01(self):
        self.upatat_log("开始检测电量")
        ele = cor.get_electricity(self.port())
        if ele == 0:
            self.upatat_log("返回码为空！")
            self.TESTING_BUT = 1
        elif ele == 1:
            self.upatat_log("端口异常！")
            self.TESTING_BUT = 1
        elif ele == 2:
            self.tableWidget.setItem(self.key_code, 3, self.fail_font())
        else:
            self.tableWidget.setItem(self.key_code, 3, self.tabel_itme_insert(ele + "%"))
            self.upatat_log("电量检测完成")

    def mcu_01(self):
        self.upatat_log("开始测试MCU引脚")
        mcu_code = cor.mcu(self.port())
        if mcu_code == 2:
            self.upatat_log("返回码为空！")
            self.TESTING_BUT = 1
        elif mcu_code == 3:
            self.upatat_log("端口异常！")
            self.TESTING_BUT = 1
        elif mcu_code == 0:
            self.tableWidget.setItem(self.key_code, 4, self.success_font())
            self.upatat_log("MCU引脚测试通过！")
            self.RESULT_01 = 0
        elif mcu_code == 1:
            self.tableWidget.setItem(self.key_code, 4, self.fail_font())
            self.upatat_log("MCU引脚测试失败！")
            self.RESULT_01 = 1

    motor_state_r = 1
    motor_state_l = 1
    def motor_01(self):
        self.COL_CODE += 1
        self.upatat_log("开始测试电机")
        code = cor.motor_test(self.port())
        if code == 0:
            self.upatat_log("电机正转成功")
            if win.comboBox.currentIndex() == 1:
                mess.label.setText("请检测锁舌是否伸出")
            else:
                mess.label.setText("请下压门锁前面板手把，门锁不可打开则通过，否则失败")
            mess.pushButton.setText("失败")
            mess.pushButton_2.setText("通过")
            mess.showDialog()
            if mess.STATE == 0:
                self.motor_state_r = 0
                self.upatat_log("电机正转测试通过！")
            elif mess.STATE == 1:
                self.motor_state_r = 1
                self.upatat_log("电机正转测试失败！")
        elif code == 2:
            self.upatat_log("返回码为空！")
            self.TESTING_BUT = 1
        elif code == 3:
            self.upatat_log("端口异常！")
            self.TESTING_BUT = 1
        else:
            self.motor_state_r = 1
            self.upatat_log("电机正转失败！")

        code = cor.motor_test_01(self.port())
        if code == 0:
            self.upatat_log("电机反转成功")
            if win.comboBox.currentIndex() == 1:
                mess.label.setText("请检测锁舌是否收回")
            else:
                mess.label.setText("请下压门锁前面板手把，门锁可打开则通过，否则失败")
            mess.pushButton.setText("失败")
            mess.pushButton_2.setText("通过")
            mess.showDialog()
            if mess.STATE == 0:
                self.motor_state_l = 0
                self.upatat_log("电机反转测试通过！")
            elif mess.STATE == 1:
                self.motor_state_l = 1
                self.upatat_log("电机反转测试失败！")
        elif code == 2:
            self.upatat_log("返回码为空！")
            self.TESTING_BUT = 1
        elif code == 3:
            self.upatat_log("端口异常！")
            self.TESTING_BUT = 1
        else:
            self.upatat_log("电机反转失败！")
            self.motor_state_l = 1

        if self.motor_state_l == 0 and self.motor_state_r == 0:
            self.tableWidget.setItem(self.key_code, self.COL_CODE, self.success_font())
            self.RESULT_02 = 0
        else:
            self.tableWidget.setItem(self.key_code, self.COL_CODE, self.fail_font())
            self.RESULT_02 = 1

    def fingerprint_01(self):
        self.COL_CODE += 1
        self.upatat_log("开始指纹头测试！")
        fin_code = cor.fingerprint_test(self.port())
        if fin_code == 0:
            self.tableWidget.setItem(self.key_code, self.COL_CODE, self.success_font())
            self.upatat_log("指纹验证成功！")
            self.RESULT_03 = 0
            time.sleep(3)
        elif fin_code == 1:
            self.tableWidget.setItem(self.key_code, self.COL_CODE, self.fail_font())
            self.upatat_log("指纹验证失败！")
            self.RESULT_03 = 1
            time.sleep(3)
        elif fin_code == 4:
            self.tableWidget.setItem(self.key_code, self.COL_CODE, self.fail_font())
            self.upatat_log("指纹头激活失败！")
            self.RESULT_03 = 1
            time.sleep(3)
        elif fin_code == 2:
            self.upatat_log("返回码为空！")
            self.TESTING_BUT = 1
        elif fin_code == 3:
            self.upatat_log("端口异常！")
            self.TESTING_BUT = 1


    def fingerprint_RGB_01(self):
        self.COL_CODE += 1
        self.upatat_log("开始测试指纹头RGB灯！")
        fingerprint_code = cor.fingerprint_RGB_test(self.port())
        self.tableWidget.horizontalScrollBar().setValue(2)
        if fingerprint_code == 0:
            self.upatat_log("指纹头RGB灯激活成功！")
            mess.label.setText("请请检测指纹头RGB灯是否亮三色灯")
            mess.pushButton.setText("失败")
            mess.pushButton_2.setText("通过")
            mess.showDialog()
            if mess.STATE == 0:
                self.upatat_log("指纹头RGB灯测试通过！")
                self.tableWidget.setItem(self.key_code, self.COL_CODE, self.success_font())
                self.RESULT_04 = 0
            elif mess.STATE == 1:
                self.tableWidget.setItem(self.key_code, self.COL_CODE, self.fail_font())
                self.upatat_log("指纹头RGB灯测试失败！！")
                self.RESULT_04 = 1
        elif fingerprint_code == 1:
            self.upatat_log("指纹头RGB灯激活失败！")
            self.tableWidget.setItem(self.key_code, self.COL_CODE, self.fail_font())
            self.RESULT_04 = 1
        elif fingerprint_code == 2:
            self.upatat_log("返回码为空！")
        elif fingerprint_code == 3:
            self.upatat_log("端口异常！")

        fingerprint_close_code = cor.fingerprint_RGB_close(self.port())
        if fingerprint_close_code == 0:
            self.upatat_log("指纹头RGB灯关闭成功！")
            time.sleep(1)
        elif fingerprint_close_code == 2:
            self.upatat_log("返回码为空！")
            self.TESTING_BUT = 1
        elif fingerprint_close_code == 3:
            self.upatat_log("端口异常！")
            self.TESTING_BUT = 1
        elif fingerprint_close_code == 1:
            self.upatat_log("指纹头RGB灯关闭失败！")
            time.sleep(1)

    def cpu_01(self):
        self.COL_CODE += 1
        self.upatat_log("开始门卡测试！")
        self.tableWidget.horizontalScrollBar().setValue(3)
        nfc_code = cor.nfc(self.port())
        if nfc_code == 0:
            self.upatat_log("门卡测试通过！")
            self.tableWidget.setItem(self.key_code, self.COL_CODE, self.success_font())
            self.RESULT_05 = 0
        elif nfc_code == 2:
            self.upatat_log("返回码为空！")
            self.TESTING_BUT = 1
        elif nfc_code == 3:
            self.upatat_log("端口异常！")
            self.TESTING_BUT = 1
        elif nfc_code == 1:
            self.tableWidget.setItem(self.key_code, self.COL_CODE, self.fail_font())
            self.upatat_log("门卡测试失败")
            self.RESULT_05 = 1

    def led_01(self):
        self.COL_CODE += 1
        self.upatat_log("开始测试呼吸灯板！")
        self.tableWidget.horizontalScrollBar().setValue(3)
        led_code = cor.led(self.port())
        if led_code == 0:
            mess.label.setText("请查看呼吸灯板是否亮红、绿两色灯光，\n且灯光光色显示均匀")
            mess.pushButton.setText("失败")
            mess.pushButton_2.setText("通过")
            mess.showDialog()
            if mess.STATE == 0:
                self.upatat_log("呼吸灯测试通过！")
                self.tableWidget.setItem(self.key_code, self.COL_CODE, self.success_font())
                self.RESULT_06 = 0
            elif mess.STATE == 1:
                self.tableWidget.setItem(self.key_code, self.COL_CODE, self.fail_font())
                self.upatat_log("呼吸灯测试失败")
                self.RESULT_06 = 1
        elif led_code == 2:
            self.upatat_log("返回码为空！")
            self.TESTING_BUT = 1
        elif led_code == 3:
            self.upatat_log("端口异常！")
            self.TESTING_BUT = 1
        elif led_code == 1:
            self.upatat_log("呼吸灯板激活失败")
            self.tableWidget.setItem(self.key_code, self.COL_CODE, self.fail_font())
            self.RESULT = 1
        cor.keyboard_RGB_close(self.port())

    def sound_01(self):
        self.COL_CODE += 1
        self.upatat_log("开始测试喇叭！")
        self.tableWidget.horizontalScrollBar().setValue(3)
        code = cor.sound(self.port())
        if code == 0:
            mess.label.setText("声音是否响亮、正常、无杂音。")
            mess.pushButton.setText("失败")
            mess.pushButton_2.setText("通过")
            mess.showDialog()
            if mess.STATE == 0:
                self.upatat_log("喇叭测试通过！")
                self.tableWidget.setItem(self.key_code, self.COL_CODE, self.success_font())
                self.RESULT_07 = 0
            elif mess.STATE == 1:
                self.tableWidget.setItem(self.key_code, self.COL_CODE, self.fail_font())
                self.upatat_log("喇叭测试失败")
                self.RESULT_07 = 1
        elif code == 2:
            self.upatat_log("返回码为空！")
            self.TESTING_BUT = 1
        elif code == 3:
            self.upatat_log("端口异常！")
            self.TESTING_BUT = 1
        elif code == 1:
            self.upatat_log("喇叭激活失败")
            self.tableWidget.setItem(self.key_code, self.COL_CODE, self.fail_font())
            self.RESULT = 1

    def keyboard_RGB_01(self):
        self.COL_CODE += 1
        self.upatat_log("开始键盘背光灯测试：")
        self.tableWidget.horizontalScrollBar().setValue(4)
        code = cor.keyboard_RGB(self.port())
        if code == 0:
            mess.label.setText("请观察门锁按键灯光是否显示均匀。")
            mess.pushButton.setText("失败")
            mess.pushButton_2.setText("通过")
            mess.showDialog()
            if mess.STATE == 0:
                self.upatat_log("按键灯测试通过")
                self.tableWidget.setItem(self.key_code, self.COL_CODE, self.success_font())
                self.RESULT_08 = 0
            elif mess.STATE == 1:
                self.tableWidget.setItem(self.key_code, self.COL_CODE, self.fail_font())
                self.upatat_log("按键背光灯测试失败")
                self.RESULT_08 = 1
        elif code == 1:
            self.upatat_log("键盘背光灯激活失败")
            self.tableWidget.setItem(self.key_code, self.COL_CODE, self.fail_font())
            self.RESULT_08 = 1
        elif code == 2:
            self.upatat_log("返回码为空！")
            self.TESTING_BUT = 1
        elif code == 3:
            self.upatat_log("端口异常！")
            self.TESTING_BUT = 1

        # 关闭键盘背光灯
        code_2 = cor.keyboard_RGB_close(self.port())
        if code_2 == 0:
            self.upatat_log("成功关闭键盘背光灯")
        elif code_2 == 1:
            self.upatat_log("键盘背光灯关闭失败")
        elif code == 2:
            self.upatat_log("返回码为空！")
            self.TESTING_BUT = 1
        elif code == 3:
            self.upatat_log("端口异常！")
            self.TESTING_BUT = 1

    def keyboard_01(self):
        self.COL_CODE += 1
        self.upatat_log("开始门锁按键测试：")
        self.tableWidget.horizontalScrollBar().setValue(5)
        t1 = threading.Thread(target=self.keyboard)
        t1.start()
        key.label.setText("请按按键：")
        key.showDialog()
        if key.STATE == 0:
            self.upatat_log("按键测试通过")
            self.tableWidget.setItem(self.key_code, self.COL_CODE, self.success_font())
            self.RESULT_09 = 0
        elif key.STATE == 1:
            self.tableWidget.setItem(self.key_code, self.COL_CODE, self.fail_font())
            self.upatat_log("按键测试失败")
            self.RESULT_09 = 1
        self.key_state = False
        time.sleep(0.5)

        if cor.keyboard_RGB_close(self.port()) == 0:
            self.upatat_log("成功关闭键盘背光灯")
        elif cor.keyboard_RGB_close(self.port()) == 1:
            self.upatat_log("键盘背光灯关闭失败")
        self.key_state = True
        key.textBrowser.clear()

    def rtc_01(self):
        self.COL_CODE += 1
        self.upatat_log("开始测试RTC！")
        self.tableWidget.horizontalScrollBar().setValue(6)
        rtc_code = cor.rtc(self.port())
        if rtc_code == 0:
            self.tableWidget.setItem(self.key_code, self.COL_CODE, self.success_font())
            self.upatat_log("RTC验证成功！")
            self.RESULT_10 = 0
        elif rtc_code == 1:
            self.tableWidget.setItem(self.key_code, self.COL_CODE, self.fail_font())
            self.upatat_log("RTC验证失败！")
            self.RESULT_10 = 1
        elif rtc_code == 2:
            self.upatat_log("返回码为空！")
            self.TESTING_BUT = 1

    def flash_01(self):
        self.COL_CODE += 1
        self.upatat_log("开始测试Flash！")
        self.tableWidget.horizontalScrollBar().setValue(7)
        flash_code = cor.flash(self.port())
        if flash_code == 0:
            self.tableWidget.setItem(self.key_code, self.COL_CODE, self.success_font())
            self.upatat_log("Flash验证成功！")
            self.RESULT_11 = 0
        elif flash_code == 1:
            self.tableWidget.setItem(self.key_code, self.COL_CODE, self.fail_font())
            self.upatat_log("Flash验证失败！")
            self.RESULT_11 = 1
        elif flash_code == 2:
            self.upatat_log("返回码为空！")
            self.TESTING_BUT = 1
        elif flash_code == 3:
            self.upatat_log("端口异常！")
            self.TESTING_BUT = 1

    def sensor_01(self):
        self.COL_CODE += 1
        self.upatat_log("开始测试Sensor！")
        self.tableWidget.horizontalScrollBar().setValue(8)
        sensor_co = cor.sensor_start(self.port())
        self.sensor_updata(sensor_co)
        t2 = threading.Thread(target=self.sensor_while)
        t2.start()
        if win.comboBox.currentIndex() == 1:
            sens.label.setText("OpenSensor：")
            sens.label_2.setText("CloseSensor：")
            sens.label_3.setText("ResetSensor：")
            sens.label_4.setText("防撬：")
            sens.label_5.setText("重置按键：")
            sens.label_6.setText("配网按键：")
            sens.label_7.setText("门磁：")
            sens.chonzhi.setText("")
            sens.menci.setText("")
            sens.peiwang.setText("")
        elif win.comboBox.currentIndex() == 0 or 2:
            sens.label.setText("防撬：")
            sens.label_2.setText("重置按键：")
            sens.label_3.setText("设置按键：")
            sens.label_4.setText("钥匙盖检测：")
            sens.label_5.setText("")
            sens.label_6.setText("")
            sens.label_7.setText("")
            sens.chonzhi.setText("")
            sens.menci.setText("")
            sens.peiwang.setText("")
        sens.showDialog()
        if sens.STATE == 0:
            self.upatat_log("Sensor测试通过")
            self.tableWidget.setItem(self.key_code, self.COL_CODE, self.success_font())
            self.RESULT_12 = 0
        elif sens.STATE == 1:
            self.tableWidget.setItem(self.key_code, self.COL_CODE, self.fail_font())
            self.upatat_log("Sensor测试失败")
            self.RESULT_12 = 1
        self.sensor_state = False
        time.sleep(0.8)

        sensot_stop_code = cor.sensor_stop(self.port())  # 结束Sensor测试
        if sensot_stop_code == 0:
            self.upatat_log("Sensor测试暂停成功")
        elif sensot_stop_code == 2:
            self.upatat_log("返回码为空！")
            self.TESTING_BUT = 1
        elif sensot_stop_code == 3:
            self.upatat_log("端口异常！")
            self.TESTING_BUT = 1
        else:
            self.upatat_log("Sensor测试暂停失败")
        self.sensor_state = True

    def clear_user_01(self):
        self.COL_CODE += 1
        self.upatat_log("开始清除设备信息！")
        flash_code = cor.clear_user_information(self.port())
        self.tableWidget.horizontalScrollBar().setValue(11)
        if flash_code == 0:
            self.tableWidget.setItem(self.key_code, self.COL_CODE, self.success_font())
            self.upatat_log("设备信息清除成功！")
            self.RESULT_13 = 0
        elif flash_code == 1:
            self.tableWidget.setItem(self.key_code, self.COL_CODE, self.fail_font())
            self.upatat_log("设备初始化失败！")
            self.RESULT_13 = 1

    sn_code = 0
    def sn_01(self):
        self.upatat_log("开始设置SN码！")
        max_code = win.lineEdit_3.text()
        min_code = win.lineEdit_2.text()
        if max_code == min_code:
            self.upatat_log("序列号已使用完，请重新设置序列号最大值。")
            self.TESTING_BUT = 1
        else:
            while len(min_code) < 5:
                min_code = "0" + min_code
            if win.comboBox.currentIndex() == 0:
                self.sn_code = "141" + self.get_SN_Time() + min_code
            elif win.comboBox.currentIndex() == 1:
                self.sn_code = "142" + self.get_SN_Time() + min_code
            elif win.comboBox.currentIndex() == 2:
                self.sn_code = "143" + self.get_SN_Time() + min_code
            sn_code = cor.set_SN(self.sn_code, self.port())
            if sn_code == 0:
                self.upatat_log("SN码设置成功！")
                self.tableWidget.setItem(self.key_code, 5, self.success_font())
                self.RESULT_14 = 0
                code3 = int(min_code)
                code3 += 1
                win.lineEdit_2.setText("{}".format(code3))
            elif sn_code == 1:
                self.upatat_log("SN码设置失败！")
                self.tableWidget.setItem(self.key_code, 5, self.fail_font())
                self.RESULT_14 = 1
            elif sn_code == 2:
                self.upatat_log("返回码为空！")
                self.TESTING_BUT = 1
            elif sn_code == 3:
                self.upatat_log("端口异常！")
                self.TESTING_BUT = 1

    def consumption_01(self):
        self.COL_CODE += 1
        self.upatat_log("开始测试功耗！")
        flash_code = cor.consumption_test(self.port())
        if flash_code == 0:
            self.upatat_log("成功进入休眠！")
            mess.label.setText("请查看功耗是否低于70uA")
            mess.pushButton.setText("失败")
            mess.pushButton_2.setText("通过")
            mess.showDialog()
            if mess.STATE == 0:
                self.upatat_log("功耗测试通过！")
                self.tableWidget.setItem(self.key_code, self.COL_CODE, self.success_font())
                self.RESULT_15 = 0
            elif mess.STATE == 1:
                self.tableWidget.setItem(self.key_code, self.COL_CODE, self.fail_font())
                self.upatat_log("功耗测试失败！")
                self.RESULT_15 = 1
        elif flash_code == 2:
            self.upatat_log("返回码为空！")
            self.TESTING_BUT = 1
        elif flash_code == 3:
            self.upatat_log("端口异常！")
            self.TESTING_BUT = 1
        else:
            self.tableWidget.setItem(self.key_code, self.COL_CODE, self.fail_font())
            self.upatat_log("门锁进入休眠失败")
            self.RESULT_15 = 1

    #  测试最终结果
    def result(self):
        self.tableWidget.horizontalScrollBar().setValue(0)  # 聚焦到当前选定格
        if self.RESULT == 0 and self.RESULT_01 == 0 and self.RESULT_02 == 0 and self.RESULT_03 == 0 \
                and self.RESULT_04 == 0 and self.RESULT_05 == 0 and self.RESULT_06 == 0 \
                and self.RESULT_07 == 0 and self.RESULT_08 == 0 and self.RESULT_09 == 0 \
                and self.RESULT_10 == 0 and self.RESULT_11 == 0 and self.RESULT_11 == 0 \
                and self.RESULT_12 == 0 and self.RESULT_13 == 0 and self.RESULT_14 == 0\
                and self.RESULT_15 == 0:
            self.tableWidget.setItem(self.key_code, 1, self.success_font())
            self.SUCCESS += 1
            self.TOTAL += 1
        else:
            self.tableWidget.setItem(self.key_code, 1, self.fail_font())
            self.FAIL += 1
            self.TOTAL += 1

    # 传入开始时间和结束时间，计算耗时
    def start_time_01(self, start, end):
        self.COL_CODE += 1  # 列数加一
        t = int(end - start)  # 结束时间戳减去开始时间戳
        div = t//60  # 时间差除以60得出商为分钟
        sec = t % 60  # 时间差除以60获取余数为秒
        self.tableWidget.setItem(self.key_code, self.COL_CODE, self.tabel_itme_insert("{}分{}秒".format(div, sec)))  # 耗时列插入耗时数据


    def state_Testing_Click(self):
        t3 = threading.Thread(target=self.run)
        t3.start()

    def run(self):
        self.pushButton.setText("测试中..")
        self.pushButton.setStyleSheet("background-color: rgb(127, 127, 127);\n"
                                      "border-radius: 10px;\n"
                                      "color: rgb(255, 255, 255);")
        self.pushButton_2.setStyleSheet("background-color: rgb(127, 127, 127);\n"
                                      "border-radius: 5px;\n"
                                      "color: rgb(255, 255, 255);")

        self.pushButton.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.textEdit.setEnabled(False)
        self.tableWidget.horizontalScrollBar().setValue(0)

        mess.label.setText("请长按重置键，点击开始测试")
        mess.pushButton_2.setText("开始测试")
        mess.pushButton.setText("取消")
        mess.showDialog()
        if mess.STATE == 0:
            start_time = time.time()  # 获取开始测试时间

            key_01 = self.key_code + 1
            self.tableWidget.setRowCount(key_01)
            self.tableWidget.setRowHeight(self.key_code, 40)
            self.tableWidget.scrollToBottom()
            go_code = cor.go_to_Testing(self.port())
            if go_code == 0:
                self.upatat_log("成功进入产测！")
                self.tableWidget.setItem(self.key_code, 0, self.tabel_itme_insert(str(key_01)))
                self.version_01()
                self.electricity_01()
                self.mcu_01()
                self.sn_01()
                for i in win.get_Testing_item():
                    if self.TESTING_BUT == 0:
                        if i == "电机测试":
                            self.motor_01()
                        if i == "指纹录入":
                            self.fingerprint_01()
                        if i == "指纹RGB":
                            self.fingerprint_RGB_01()
                        if i == "门卡测试":
                            self.cpu_01()
                        if i == "呼吸灯测试":
                            self.led_01()
                        if i == "喇叭测试":
                            self.sound_01()
                        if i == "键盘背光":
                            self.keyboard_RGB_01()
                        if i == "按键触摸":
                            self.keyboard_01()
                        if i == "RTC测试":
                            self.rtc_01()
                        if i == "Flash测试":
                            self.flash_01()
                        if i == "Sensor测试":
                            self.sensor_01()
                        if i == "设备初始化":
                            self.clear_user_01()
                        if i == "功耗测试":
                            self.consumption_01()
                    else:
                        break
                end_time = time.time()  # 获取程序结束时间

                if self.TESTING_BUT == 0:
                    self.start_time_01(start_time, end_time)  # 调用start_time_01传入开始时间和结束时间
                    self.result()  # 调用result()方法写入最终测试结果

                    ct = time.time()
                    local_time = time.localtime(ct)
                    data_head = time.strftime("%Y%m%d", local_time)
                    product_name = win.comboBox.currentText()

                    data = []
                    row = self.tableWidget.rowCount()
                    column = self.tableWidget.columnCount()
                    data_row = []
                    for i in range(0, column):
                        data_row.append(self.tableWidget.item(row - 1, i).text())
                    data_row.append(win.get_current_time())
                    data_row.append(self.sn_code + "，")
                    data.append(data_row)
                    file_name = './log/{}{}.xlsx'.format(data_head, product_name)
                    if os.path.isfile(file_name):
                        df = pd.read_excel(file_name)
                        if product_name == "玻璃门锁C1S" and column == 18:
                            try:
                                df.loc[len(df)] = data[0]
                                df.to_excel(file_name, index=False)
                            except Exception as e:
                                self.upatat_log("请关闭记录文件，否则无法正常保存记录。")
                        elif product_name == "LineHope智能门锁S2" and column == 20:
                            try:
                                df.loc[len(df)] = data[0]
                                df.to_excel(file_name, index=False)
                            except Exception as e:
                                self.upatat_log("请关闭记录文件，否则无法正常保存记录。")
                        elif product_name == "方舟鱼智能门锁S2" and column == 20:
                            try:
                                df.loc[len(df)] = data[0]
                                df.to_excel(file_name, index=False)
                            except Exception as e:
                                self.upatat_log("请关闭记录文件，否则无法正常保存记录。")

                    else:
                        self.upatat_log("文件不存在！")
                    self.set_num("code", "min", win.lineEdit_2.text())
                self.key_code += 1
            elif go_code == 1:
                self.upatat_log("进入产测失败！")
            elif go_code == 2:
                self.upatat_log("请按住门锁重置按键后点击开始测试！")
            elif go_code == 3:
                self.upatat_log("端口异常！")
            self.upatat_log("-----------------------------------------")
        elif mess.STATE == 1:
            pass
        self.tableWidget.horizontalScrollBar().setValue(0)
        self.COL_CODE = 5
        self.RESULT = 0
        self.RESULT_01 = 0
        self.RESULT_02 = 0
        self.RESULT_03 = 0
        self.RESULT_04 = 0
        self.RESULT_05 = 0
        self.RESULT_06 = 0
        self.RESULT_07 = 0
        self.RESULT_08 = 0
        self.RESULT_09 = 0
        self.RESULT_10 = 0
        self.RESULT_11 = 0
        self.RESULT_12 = 0
        self.RESULT_13 = 0
        self.RESULT_14 = 0
        self.RESULT_15 = 0
        self.TESTING_BUT = 0
        self.label_2.setText("{}".format(self.TOTAL))
        self.label_3.setText("{}".format(self.SUCCESS))
        self.label_4.setText("{}".format(self.FAIL))
        self.pushButton.setText("开始测试")
        self.pushButton.setStyleSheet("background-color: rgb(75, 115, 177);\n"
                                      "border-radius: 10px;\n"
                                      "color: rgb(255, 255, 255);")
        self.pushButton_2.setStyleSheet("background-color: rgb(75, 115, 177);\n"
                                        "border-radius: 5px;\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(True)
        self.textEdit.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cor = Cor()
    win = Login()  # 创建登录界面实例化
    home = Home_Page()
    mess = Message_Page()
    key = KeyBoard_Page()
    sens = Sensor_Page()
    sys.exit(app.exec_())