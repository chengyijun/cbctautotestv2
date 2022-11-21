# -*- coding:utf-8 -*-
# 作者: 程义军
# 时间: 2022/11/14 10:53
from time import sleep

from PyQt5.QtCore import QThread

from ct import CT
from dx import DX
from px import PX
from tmj import TMJ
from utils import select_app, add_patient, read_config_data


class AutoTest(QThread):
    """
    自动化测试逻辑
    """

    def __init__(self, parent=None) -> None:
        super().__init__(parent)

    def run(self) -> None:
        self.task()

    def task(self):
        ct_loop_count = int(float(tmp1)) if (tmp1 := self.parent().lineEdit.text()) != "" else 0
        px_loop_count = int(float(tmp2)) if (tmp2 := self.parent().lineEdit_2.text()) != "" else 0
        dx_loop_count = int(float(tmp3)) if (tmp3 := self.parent().lineEdit_3.text()) != "" else 0
        tmj_loop_count = int(float(tmp4)) if (tmp4 := self.parent().lineEdit_4.text()) != "" else 0
        wait_duration = int(float(tmp5)) if (tmp5 := self.parent().lineEdit_5.text()) != "" else read_config_data().get(
            "wait_pre_shot")
        print(ct_loop_count, px_loop_count, dx_loop_count, tmj_loop_count, wait_duration)

        for i in range(1, ct_loop_count + 1):
            print("ct测试")
            ct = CT()
            select_app()
            add_patient("ct", i)
            ct.image_collect()
            sleep(wait_duration)

        for i in range(ct_loop_count + 1, ct_loop_count + px_loop_count + 1):
            print("px测试")
            px = PX()
            select_app()
            add_patient("px", i)
            px.image_collect()
            sleep(wait_duration)

        for i in range(ct_loop_count + px_loop_count + 1, ct_loop_count + px_loop_count + dx_loop_count + 1):
            print("dx测试")
            dx = DX()
            select_app()
            add_patient("dx", i)
            dx.image_collect()
            sleep(wait_duration)

        for i in range(ct_loop_count + px_loop_count + dx_loop_count + 1,
                       ct_loop_count + px_loop_count + dx_loop_count + tmj_loop_count + 1):
            print("tmj测试")
            tmj = TMJ()
            select_app()
            add_patient("tmj", i)
            tmj.image_collect()
            sleep(wait_duration)
