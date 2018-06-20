# coding=utf-8

'''
你在长途旅行，刚到一个加油站，距下一个加油站还有200km。编写一个程序确定是不是需要在这里加油，还是可以等到下一个加油站再加油。
这个程序应当问下面几个问题。
    你的油箱有多大（单位是升）？
    油箱有多满（按百分比、例如，半满就是50%）？
    你的汽车每升油可以走多远（km）？

    输出应该像这样：
        Size of tank:60
        percent full:40
        km per liter:10
        You can go another 240 km
        The next gas station is 200 km away
        You can wait for the next stantion.
    或
    	Size of tank:60
        percent full:30
        km per liter:8
        You can go another 144 km
        The next gas station is 200 km away
        Get gas now!

    额外提示：程序中包含一个5升的缓冲区，以防油表不准。
'''

tank = float(raw_input('Size of tank:'))
percent = float(raw_input('percent full:'))
km = float(raw_input('km per liter:'))
go = percent / 100 * (tank - 5) * km

if go >= 200:
    print 'You can go another', go, 'km'
    print 'The next gas station is 200 km away'
    print 'You can wait for the next stantion.'
else: 
    print 'You can go another', go, 'km'
    print 'The next gas station is 200 km away'
    print 'Get gas now!'
