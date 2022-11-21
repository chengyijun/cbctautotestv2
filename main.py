# -*- coding:utf-8 -*-
# 作者: 程义军
# 时间: 2022/11/11 9:19
import sys

from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication
from system_hotkey import SystemHotkey

from autotest import AutoTest
from ui.main_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    绘制软件界面
    """
    # 自定义 全局快捷键关闭窗口的信号
    my_closed = pyqtSignal(bool)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("老化测试软件V2.0")
        # 全局快捷键
        self.set_global_hotkey()

    @pyqtSlot()
    def on_pushButton_clicked(self):
        print("start")
        auto_test = AutoTest(parent=self)
        auto_test.start()

    def set_global_hotkey(self):
        # 2. 设置我们的自定义热键响应函数
        self.my_closed.connect(self.hk_handler)
        # 3. 创建快捷键
        self.hk_close = SystemHotkey()
        # 4. 为快捷键绑定处理函数
        self.hk_close.register(('control', '1'), callback=lambda x: self.send_key_event())

    def send_key_event(self):
        self.my_closed[bool].emit(True)

    def hk_handler(self, is_close: bool):
        if is_close:
            self.close()


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()

    main_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
