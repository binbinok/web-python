# coding=utf-8
import easygui

# flavor = easygui.buttonbox('what is your favorite ice cream flavor?', choices=['Vanilla', 'Chocolate', 'Strawberry'])
# flavor = easygui.choicebox('what is your favorite ice cream flavor?', choices=['Vanilla', 'Chocolate', 'Strawberry'])
flavor = easygui.enterbox('what is your favorite ice cream flavor?')
# print easygui.passwordbox('请输入密码')
easygui.msgbox('You picked ' + flavor)