# -*- coding:utf-8 -*-
# 作者: 程义军
# 时间: 2022/11/11 9:19
import sys
from time import sleep

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication

from ct import CT
from ui.main_ui import Ui_MainWindow
from utils import select_app, add_patient, read_config_data


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("老化测试软件V2.0")

    @pyqtSlot()
    def on_pushButton_clicked(self):
        print("start")
        ct_loop_count = int(float(tmp1)) if (tmp1 := self.lineEdit.text()) != "" else 0
        px_loop_count = int(float(tmp2)) if (tmp2 := self.lineEdit_2.text()) != "" else 0
        dx_loop_count = int(float(tmp3)) if (tmp3 := self.lineEdit_3.text()) != "" else 0
        tmj_loop_count = int(float(tmp4)) if (tmp4 := self.lineEdit_4.text()) != "" else 0
        wait_duration = int(float(tmp5)) if (tmp5 := self.lineEdit_5.text()) != "" else read_config_data().get(
            "wait_pre_shot")
        print(ct_loop_count, px_loop_count, dx_loop_count, tmj_loop_count, wait_duration)

        for i in range(ct_loop_count):
            print("ct测试")
            ct = CT()
            select_app()
            add_patient()
            ct.image_collect()
            sleep(wait_duration)

        for i in range(px_loop_count):
            print("px测试")

        for i in range(dx_loop_count):
            print("dx测试")

        for i in range(tmj_loop_count):
            print("tmj测试")


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()

    main_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
