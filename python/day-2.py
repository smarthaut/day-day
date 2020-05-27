#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/18 下午5:33
# @Author  : huanghe
# @Site    : 
# @File    : day-2.py
# @Software: PyCharm

"""
python递归的最大层数？
mac:997

求结果：
    v1 = 1 or 3 ==>1
    v2 = 1 and 3  ==>3
    v3 = 0 and 2 and 1==>0
     v4 = 0 and 2 or 1 ==>1
     v5 = 0 and 2 or 1 or 4==>1
     v6 = 0 or Flase and 1

# and中含0，返回0； 均为非0时，返回后一个值，
# or中， 至少有一个非0时，返回第一个非0,

ascii、unicode、utf-8、gbk 区别？
最开始的ascii码128位，为了统一出现unicode

字节码和机器码的区别？
机器码就是说计算机能读懂的代码,简单点说就是给计算机执行的二进制代码.
字节码,是JAVA语言专有的,它是让JVM来执行的二进制代码

三元运算规则以及应用场景？
a=5 if true else 6

列举 Python2和Python3的区别？

 1、print

            在python2中，print被视为一个语句而不是一个函数，python3中，print()被视为一个函数
2、整数的除法

            在python2中，键入的任何不带小数的数字，将被视为整数的编程类型。比如5/2=2，解决方法：5.0/2.0=2.5

            在python3中，整数除法变得更直观 5/2=2.5

3、Unicode

            Python 2 默认使用 ASCII 字母表；Python 3 默认使用 Unicode
用一行代码实现数值交换：
       a = 1
       b = 2

 a,b = b,a
"""

def get_max_foo(n):
    print(n)
    n= n+1
    get_max_foo(n)



if __name__ =="__main__":
    print(0 or True and 1)

