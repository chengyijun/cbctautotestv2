# -*- coding:utf-8 -*-
# 作者: 程义军
# 时间: 2022/11/11 9:19
import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication

from autotest import AutoTest
from ui.main_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    绘制软件界面
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("老化测试软件V2.0")

    @pyqtSlot()
    def on_pushButton_clicked(self):
        print("start")
        auto_test = AutoTest(parent=self)
        auto_test.start()


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()

    main_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
