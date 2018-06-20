# coding=utf-8

'''
    编写一个程序，显示一个乘法表。开始时要询问用户显示哪个数的乘法表。输出应该如下所示：
        Which multiplication table would you like? 5
        Here's your table:
        5 * 1 = 5
        5 * 2 = 10
        5 * 3 = 15
        5 * 4 = 20
        5 * 5 = 25
        5 * 6 = 30
        5 * 7 = 35
        5 * 8 = 40
        5 * 9 = 45
        5 * 10 = 50
'''

num = int(raw_input('Which multiplication table would you like?'))


for i in range(1, 11):
    print num, '*', i, '=', num * i