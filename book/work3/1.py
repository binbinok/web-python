
# 使用交互模式或者编写一个小程序解决下面的问题。
# （a）3个人在餐厅吃饭，相分摊饭费。总共花费35.27美元。他们还想留15%的小费。每个人该怎么付钱？
# （b）计算一个12.5m * 16.7m的矩形房间的面积和周长。


total = 35.27
number = 3
tip = 0.15
print('每人付', (total + total * tip) / number, '美元')

l = 12.5
w = 16.7
print('12.5m*16.7m的矩形房间的面积为', l * w, '周长为', (l + w) * 2)