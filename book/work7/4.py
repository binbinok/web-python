# coding=utf-8

'''
    建立一个程序，用户必须输入密码才能使用这个程序。你当然知道密码（因为它会写在你的代码中）。不过，你的朋友要得到这个密码就必须问你或者直接猜，也可以学习足够的Python知识查看代码来找出密码！

    对程序没什么要求，可以是你已经编写的程序，也可以是一个非常简单的程序，只在用户输入正确的口令时显示条“You're in!”之类的消息。
'''

import easygui

PASSWORD = '123qwe'
password = easygui.passwordbox()

if PASSWORD == password:
    easygui.msgbox("You're in!")