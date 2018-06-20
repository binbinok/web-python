# coding=utf-8
# 试着使用int()从一个字符串创建整数。要保证结果确实是一个整数！

string = '14.65'
fl = float(string)
num = int(fl)

print ('num:', num, 'type', type(num))