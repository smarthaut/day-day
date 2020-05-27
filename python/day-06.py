#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/25 上午9:26
# @Author  : huanghe
# @Site    : 
# @File    : day-06.py
# @Software: PyCharm
def num():
    return [lambda x: i*x for i in range(4)]

for i in num():
    print(i(1))

#列举常见的内置函数？
#sorted  max min map reduce

#filter、map、reduce的作用？

#filter(函数，可迭代对象) :筛选

def is_even(num):
    if num % 2 == 0:
        return num

for i in filter(is_even, [1,2,3,4]):
    print(i)
    
#map
def obj(n):
    return n * n
print(list(map(obj,[1,2,3,4])))

#reduce 压缩运算
from functools import reduce
def obj(m,n):
    return m * n
print(reduce(obj,[1,2,3,4]))


#一行代码实现9*9乘法表


print("\n".join("\t".join(["%s*%s=%s"%(x, y, x*y) for y in range(1, x + 1)])for x in range(1, 10)))
    

