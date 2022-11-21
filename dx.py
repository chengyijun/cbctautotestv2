# -*- coding:utf-8 -*-
# 作者: 程义军
# 时间: 2022/11/11 10:58
from time import sleep

from utils import wait_until_checkpoint_appear, select_app, click_action, get_pos, shift_action, add_patient, \
    read_config_data


class DX:

    def image_collect(self):
        # 切换tab 到【影像信息】
        click_action(*get_pos('image_info'))
        # 点击 模式选择 下拉框
        click_action(*get_pos('model_select'))
        # 切换到【dx】模式
        shift_action(*get_pos('dx_shift'))
        # 点击 【立即拍片】
        click_action(*get_pos('shoot'))

        print("进入采集界面")
        wait_until_checkpoint_appear("cp1_jqzb.png")
        # 点击【机器准备】
        sleep(read_config_data().get("wait_before_ready"))
        click_action(*get_pos('machine_ready'))
        print("确认拍摄检查点")
        wait_until_checkpoint_appear("cp2_qrps.png")
        sleep(read_config_data().get("wait_before_take_shot"))
        # 点击【确认拍摄】
        click_action(*get_pos('take_shot'))
        print("完成拍摄检查点")
        sleep(read_config_data().get("wait_before_finish_take_shot"))
        wait_until_checkpoint_appear("cp3_wcps.png")
        # 点击【完成拍摄】
        click_action(*get_pos('finish_take_shot'))
        print("拍片完成")
        sleep(read_config_data().get("wait_after_finish_take_shot"))


def main():
    dx = DX()
    select_app()
    add_patient(1)
    dx.image_collect()


if __name__ == '__main__':
    main()
