# coding=utf-8
'''
    一家商场在降价促销。如果购买金额低于或等于10元，会给10%的折扣，如果购买金额大于10元，会给20%的折扣。编写一个程序，询问购买价格，再显示折扣（10%或20%）和最终价格
'''

price = float(raw_input('输入价格'))

if price <= 10 :
    print '您将享受10%的折扣，最终价格为：', price * 0.9
else:
    print '您将享受20%的折扣，最终价格为：', price * 0.8
