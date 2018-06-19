# coding=utf-8

# 试着修改第5章中的温度转换程序，这一次要用GUI输入和输出而不是raw_input()和print。

import easygui

f = easygui.integerbox('输入华氏度', upperbound=100000)
s = float('%.2f' % (5.0 / 9))

easygui.msgbox(s * (f - 32))