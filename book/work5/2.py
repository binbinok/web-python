# coding=utf-8
# 编辑一个程序询问一间长方形房间的尺寸（单位是米），然后计算覆盖整个房间总共需要多少地毯，并显示出来。

'''
编辑一个程序先完成上面的要求，不过还要询问每平方尺地毯的价格。然后主程序显示下面3个内容：
    总共需要多少地毯，单位是平方米。
    总共需要多少地毯，单位是平方尺（1平方米=9平方尺）
    地毯总价格。
'''

length = float(raw_input('房间长度是多少？'))
width = float(raw_input('房间宽度是多少？'))
price = float(raw_input('地毯一平方尺的价格是多少？'))
area = length * width

print '房间总共需要',
print area,
print '平方米地毯 ',
print area * 9,
print '平方尺地毯',
print '总价格',
print area * 9 * price

