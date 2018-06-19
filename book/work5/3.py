# coding=utf-8
'''
编辑一个程序帮助用户统计她的零钱。
程序要问下面的问题。
    “有多少个五分币？”
    “有多少个二分币？”
    “有多少个一分币？”
让程序给出这些零钱的总面值。
'''

value5 = int(raw_input('有多少个五分币？'))
value2 = int(raw_input('有多少个二分币？'))
value1 = int(raw_input('有多少个一分币？'))

print '总面值是',
print (5 * value5) + (2 * value2) + (1 * value1)