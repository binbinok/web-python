# coding=utf-8

'''
    一个足球队在寻找年龄在10到12岁之间的小女孩加入。编写一个程序，询问用户的年龄和性别（m表示男性，f表示女性）。显示一条消息指出这个人是否可以加入球队。
'''

import easygui as gui

age = gui.integerbox('请输入你的年龄')
sex = gui.choicebox('请选择你的性别', choices=['m', 'f'])
print sex
if 10 <= age <= 12 and sex == 'f':
    print '恭喜你可以加入球队!'
else:
    print '很遗憾你不能加入球队'
