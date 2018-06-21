#  coding=utf-8

'''
    根据第1题写的程序，让它除了打印各个数之外还要打印一行星号，如下：
        Countdown timer: Gow many seconds? 4
        4 ****
        3 ***
        2 **
        1 *
        BLAST OFF!
    
    （提示：可能需要使用一个嵌套循环。）
'''

import time

t = int(raw_input('Countdown timer: How many seconds?'))

for i in range(t, 0, -1):
    print i, 
    for j in range(i):
        print '*',
    time.sleep(1)
print "BLAST OFF!"

