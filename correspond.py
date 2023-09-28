import re

import serial
import time
import binascii
import serial.tools.list_ports


class Cor:

    start = True
    # 获取端口号
    # def get_port(self):
    #     try:
    #         ports_list = list(serial.tools.list_ports.comports())
    #         len1 = len(ports_list)
    #         i = 0
    #         while i < len1:
    #             comAttr1 = list(ports_list[i])
    #             port = comAttr1[0]
    #             i += 1
    #             if comAttr1[1] == 'USB-SERIAL CH340 (' + port + ')':
    #                 return port
    #             else:
    #                 print(comAttr1[1])
    #                 return 1
    #     except Exception as e:
    #         print(e)
    #         raise

    # 获取端口列表返回到界面combobox控件显示
    def get_port_01(self):
        try:
            ports_list = list(serial.tools.list_ports.comports())
            len1 = len(ports_list)
            i = 0
            port_list_01 = []
            while i < len1:
                comAttr1 = list(ports_list[i])
                i += 1
                port_list_01.append(comAttr1[1])
            return port_list_01
        except Exception as e:
            print(e)
            raise

    def send_data(self, data, t, port):
        bps = 115200  # 设置波特率
        timex = 1  # 设置超时时间
        try:
            ser = serial.Serial(port, bps, timeout=timex)
            try:
                b = bytes.fromhex(data)
                ser.write(b)
                time.sleep(t)
                count = ser.inWaiting()
                if count > 0:
                    data = ser.read(count)
                    if data != b'':
                        return str(binascii.b2a_hex(data))[2:-1]
                else:
                    return 0  # 返回码为空
                ser.close()

            except serial.SerialTimeoutException:
                pass
            finally:
                ser.close()
        except Exception as e:
            return 1  # 返回1代表端口异常常

    # 累加和
    def data_sum(self, data8):
        o = []
        while len(data8) > 0:
            op = data8[:2]
            o.append(op)
            data8 = data8[2:]
        check_sum_str = hex(sum([int(i, 16) for i in o]))
        data9 = check_sum_str[-2:]
        return data9.upper()

    # 接收返回指令
    def receive(self, timex, port):
        bps = 115200  # 设置波特率
        ser = serial.Serial(port, bps, timeout=timex)
        try:
            time.sleep(timex)
            count = ser.inWaiting()
            if count > 0:
                data = ser.read(count)
                if data != b'':
                    return str(binascii.b2a_hex(data))[2:-1]
            ser.close()
        except serial.SerialTimeoutException:
            pass
        finally:
            ser.close()

    def receive01(self, port):
        bps = 115200  # 设置波特率
        ser = serial.Serial(port, bps, timeout=0.5)
        try:
            while self.start is True:
                count = ser.inWaiting()
                if count > 0:
                    data = ser.read(count)
                    if data != b'':
                        self.start = False
                        return str(binascii.b2a_hex(data))[2:-1]
            ser.close()
        except serial.SerialTimeoutException:
            pass
        finally:
            ser.close()

    # 进入产测模式
    def go_to_Testing(self, port):
        key = "434D44700070"
        code = self.send_data(key, 0.2, port)
        if code == 0:
            return 2
        elif code == 1:
            return 3
        elif code == "434d44700070":
            return 3
        else:
            if code[-4:-2] == "01":
                return 1
            elif code[-4:-2] == "00":
                return 0

    def exit_Testing(self, port):
        key = "434D44710071"
        code = self.send_data(key, 0.2, port)
        if code is None:
            pass
        else:
            if code[-4:-2] == "01":
                return 1
            elif code[-4:-2] == "00":
                return 0

    # 获取固件版本号
    def version(self, port):
        key = "43 4D 44 85 00 85"
        code = self.send_data(key, 0.2, port)[10:-2]
        a = []
        if code == 0:
            return 0
        elif code == 1:
            return 1
        else:
            while len(code) > 0:
                num = code[:2]
                if num == 'ff':
                    pass
                else:
                    a.append(str(int(num) - 30))
                code = code[2:]
            c = "".join(a)
            return c

    # 获取门锁电量
    def get_electricity(self, port):
        key = "43 4D 44 84 00 84"
        code = self.send_data(key, 0.5, port)
        if code == 0:
            return 0
        elif code == 1:
            return 1
        elif code[:8] == "4e544684":
            ele = code[-4:-2]
            return ele
        else:
            return 2

    # BLE发射功率
    def ble(self, port):
        key = "43 4D 44 87 00 87"
        code = self.send_data(key, 0.5, port)

    # 获取BLE版本号
    def get_ble_version(self, port):
        key = "43 4D 44 86 00 86"
        self.send_data(key, 0.5, port)

    # MCU引脚测试
    def mcu(self, port):
        key_low = "43 4D 44 82 01 00 83"
        key_tall = "43 4D 44 82 01 01 84"
        code_low = self.send_data(key_low, 0.5, port)
        code_tall = self.send_data(key_tall, 0.5, port)
        if code_low == 0 or code_tall == 0:
            return 2
        elif code_low == 1 or code_tall == 1:
            return 3
        else:
            if code_low[-4:-2] == "00" and code_tall[-4:-2] == "00":
                return 0
            else:
                return 1

    # 电机测试反转开锁
    def motor_test(self, port):
        key = "43 4D 44 77 01 01 79"
        code = self.send_data(key, 2, port)
        if code == 0:
            return 2  # 返回码为空
        elif code == 1:
            return 3  # 端口异常
        else:
            if code[10:12] == "00" or "02":
                return 0
            elif code[10:12] == "01":
                return 1

    # 电机测试正转关锁
    def motor_test_01(self, port):
        key = "43 4D 44 77 01 00 78"
        code = self.send_data(key, 2, port)
        if code == 0:
            return 2
        elif code == 1:
            return 3
        else:
            if code[10:12] == "00" or "02":
                return 0
            elif code[10:12] == "01":
                return 1

    # 指纹模组测试
    def fingerprint_test(self, port):
        key = "43 4D 44 72 00 72"
        key_2 = "43 4D 44 73 00 73"
        code_1 = self.send_data(key, 0.5, port)
        if code_1 == 0:
            return 2
        elif code_1 == 1:
            return 3
        else:
            if code_1[-4:-2] == "00":
                code2 = self.receive01(port)
                # print(code2)
                self.start = True
                if code2[10:12] == "00":
                    self.send_data(key_2, 0.5, port)
                    return 0
                else:
                    self.send_data(key_2, 0.5, port)
                    return 1
            elif code_1[-4:-2] == "01":
                self.send_data(key_2, 0.5, port)
                return 4

    # 指纹RGB测试
    def fingerprint_RGB_test(self, port):
        key = "43 4D 44 74 00 74"
        code = self.send_data(key, 0.5, port)
        if code == 0:
            return 2
        elif code == 1:
            return 3
        else:
            if code[-4:-2] == "00":
                return 0
            elif code[-4:-2] == "01":
                return 1

    # 关闭指纹头RGB灯
    def fingerprint_RGB_close(self, port):
        key = "43 4D 44 81 00 81"
        code = self.send_data(key, 0.5, port)
        if code == 0:
            return 2
        elif code == 1:
            return 3
        else:
            if code[-4:-2] == "00":
                return 0
            elif code[-4:-2] == "01":
                return 1

    # 卡片测试
    def nfc(self, port):
        key = "43 4D 44 8E 00 8E"
        self.send_data(key, 0.5, port)
        code = self.receive01(port)
        self.start = True
        if code == 0:
            return 2
        else:
            if code[10:12] == "00":
                return 0
            else:
                return 1

    # 灯板呼吸灯测试
    def led(self, port):
        key = "43 4D 44 8F 00 8F"
        code = self.send_data(key, 0.5, port)
        if code == 0:
            return 2
        elif code == 1:
            return 3
        else:
            if code[-4:-2] == "00":
                return 0
            elif code[-4:-2] == "01":
                return 1

    # 声音测试
    def sound(self, port):
        key = "43 4D 44 75 00 75"
        code = self.send_data(key, 2, port)
        if code == 0:
            return 2
        elif code == 1:
            return 3
        else:
            if code[-4:-2] == "00":
                return 0
            elif code[-4:-2] == "01":
                return 1

    # 键盘背光灯测试
    def keyboard_RGB(self, port):
        key = "43 4D 44 78 00 78"
        code = self.send_data(key, 1, port)
        if code == 0:
            return 2
        elif code == 1:
            return 3
        else:
            if code[-4:-2] == "00":
                return 0
            elif code[-4:-2] == "01":
                return 1

    # 关闭键盘背光灯
    def keyboard_RGB_close(self, port):
        key = "43 4D 44 79 00 79"
        code = self.send_data(key, 0.5, port)
        if code == 0:
            return 2
        elif code == 1:
            return 3
        else:
            if code[-4:-2] == "00":
                return 0
            elif code[-4:-2] == "01":
                return 1

    # RTC测试
    def rtc(self, port):
        t = (hex(int(time.time())))[2:]
        sun = str(self.data_sum("7A04" + str(t)))
        key = "434D447A04{}".format(t + sun)
        self.send_data(key, 0.5, port)
        code = self.receive01(port)
        self.start = True
        if code is None:
            return 2
        else:
            if int(code[-4:-2]) < 5:
                return 0
            elif int(code[-4:-2]) > 5:
                return 1

    # Flash测试
    def flash(self, port):
        key = "434D447B007B"
        code = self.send_data(key, 0.5, port)
        if code == 0:
            return 2
        elif code == 1:
            return 3
        else:
            if int(code[-4:-2]) < 5:
                return 0
            elif int(code[-4:-2]) > 5:
                return 1

    # 开始Sensor测试
    def sensor_start(self, port):
        key_start = "43 4D 44 88 00 88"  # 开始sensor测试
        key_select = "43 4D 44 7F 00 7F"  # Sensor开关查询
        self.send_data(key_start, 0.5, port)  # 开始sensor测试
        code = self.send_data(key_select, 0.5, port)
        return code[10:-2]  # 4e54467f0a   01 00 00 01 ff 00 01 01 ff ff 8a

    # 结束Sensor测试
    def sensor_stop(self, port):
        key_stop = "43 4D 44 89 00 89"  # 结束sensor测试
        code = self.send_data(key_stop, 0.5, port)  # 开始sensor测试
        if code == "4e5446890089":
            return 0
        elif code == 0:
            return 2
        elif code == 1:
            return 3
        else:
            return 1

    # 清空用户信息
    def clear_user_information(self, port):
        key = "43 4D 44 8A 00 8A"
        self.send_data(key, 0.5, port)
        code = self.receive01(port)
        self.start = True
        if code == "4e54468a008a":
            return 0
        else:
            return 1

    # 设置SN号
    def set_SN(self, data, port):
        data_list = []
        for i in data:
            data_list.append(str(int(i) + 30))
        num = "8B0C{}".format("".join(data_list))
        key = "434D44{}".format(num + self.data_sum(num))
        code = self.send_data(key, 0.5, port)
        if code == 0:
            return 2
        elif code == 1:
            return 3
        else:
            if code == "4e54468b008b":
                return 0
            else:
                return 1

    # 功耗测试
    def consumption_test(self, port):
        key = "43 4D 44 80 00 80"
        code = self.send_data(key, 0.5, port)
        if code == 0:
            return 2
        elif code == 1:
            return 3
        else:
            if code[-4:-2] == "00":
                return 0
            elif code[-4:-2] == "01":
                return 1

    # 获取模块MAC地址
    def get_BLE_MAC(self, port):
        key = "43 4D 44 86 00 86"
        code = self.send_data(key, 0.5, port)
        print(code)
        if code == 0:
            return 2
        elif code == 1:
            return 3
        else:
            if code[-4:-2] == "00":
                return 0
            elif code[-4:-2] == "01":
                return 1


if __name__ == '__main__':
    cor = Cor()
    cor.get_BLE_MAC("COM11")
    # print(cor.go_to_Testing("COM11"))
    # cor.ble()
    # print(cor.motor_test())
    # print(cor.motor_test_01())
    # print(cor.mcu())
    # print(cor.get_electricity())
    # print(cor.fingerprint_RGB_test("COM11"))
    # time.sleep(4)
    print(cor.fingerprint_RGB_close("COM11"))
    # time.sleep(5)
    # print(cor.fingerprint_test("COM11"))
    # time.sleep(5)
    # print(cor.sound("COM11"))
    # time.sleep(2)
    # print(cor.keyboard_RGB())
    # cor.keyboard_RGB_close()
    # print(cor.rtc())
    # print(cor.flash())
    # print(cor.version())
    # cor.sensor()
    # print(cor.led())
    # print(cor.clear_user_information())
    # print(cor.receive(10))
    # print(cor.set_SN("141220800111"))
    # print(cor.exit_Testing())
    # print(cor.get_port())
    # print(cor.sensor_stop())
    # print(cor.nfc())
    # print(cor.get_port())
    # print(cor.receive01())
    # print(cor.get_port_01())