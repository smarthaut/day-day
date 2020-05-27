#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/13 上午10:01
# @Author  : huanghe
# @Site    : 
# @File    : day-01.py
# @Software: PyCharm

#1Python语言？

"""
python:是一种解释型、面向对象、动态数据类型的高级程序设计语言。属于解释型语言（java）
C、C++、Objective等都属于编译型语言
"""
#2 Python解释器种类以及特点？
"""
CPython
c语言开发的 使用最广的解释器
IPython
基于cpython之上的一个交互式计时器 交互方式增强 功能和cpython一样
PyPy
目标是执行效率 采用JIT技术 对python代码进行动态编译，提高执行效率
JPython
运行在Java上的解释器 直接把python代码编译成Java字节码执行
IronPython
运行在微软 .NET 平台上的解释器，把python编译成. NET 的字节码

"""
#3 位和字节的关系
"""
位:bit
一个二进制数据0或1,是计算机传输的最小单元.8位组成一个字节.

字节:byte
存储空间的计量单元,1个字节有8个bit.而1024个字节又代表1K
"""

#4 请至少列举5个 PEP8 规范
"""
每一级缩进使用4个空格。
类名一般使用首字母大写的约定
导入通常在分开的行
所有行限制的最大字符数为79
永远不要使用字母‘l’（小写的L），‘O’（大写的O），或者‘I’（大写的I）作为单字符变量名
"""
#5 通过代码实现如下转换：
#二进制转换成十进制：v = “1111011”
def bin2dec(num):
    print(int(num))

bin2dec(0b1111011)


# 十进制转换成二进制：v = 18

def dec2bin(num):
    print(bin(num))
    
dec2bin(18)


