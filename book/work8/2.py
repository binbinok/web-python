# coding=utf-8

'''
    完成第1题的程序时你可能使用了for循环。大多数人都会这么做。不过，可以再做个练习，试着用while循环完成同样的工作。或者如果你在第1题中使用了while循环，现在可以试着用for循环来完成。
'''

num = int(raw_input('Which multiplication table would you like?'))
i = 1

while i <= 10:
    print num, '*', i, '=', num * i
    i += 1