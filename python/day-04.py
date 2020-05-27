#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/21 上午10:44
# @Author  : huanghe
# @Site    : 
# @File    : day-04.py
# @Software: PyCharm
"""

列举布尔值为False的常见值？
NULL 0 [] {} ()

字符串、列表、元组、字典每个常用的5个方法？

lambda表达式格式以及应用场景？

pass的作用？

*arg和**kwarg作用
"""

# 字符串
words = "today is a wonderfulday"
print(words.strip('today'))      # 如果strip方法指定一个值的话，那么会去掉这两个值
print(words.count('a'))          # 统计字符串出现的次数
print(words.index('i'))         # 找下标
print(words.replace('day','DAY'))# 字符串替换
#
# # 列表
sample_list = ['a', 1, ('a', 'b')]  # 创建列表
sample_list = ['a', 'b', 0, 1, 3]   #  Python列表操作
value_start = sample_list[0]  # 得到列表中的某一个值
end_value = sample_list[-1]  # 得到列表中的某一个值
del sample_list[0]  # 删除列表的第一个值
sample_list[0:0] = ['sample value']  # 在列表中插入一个值

# 元组
#元组也是一个list，他和list的区别是元组的元素无法修改
tuple1 = (2, 3, 4, 5, 6, 4, 7)
print(type(tuple1))
print(tuple1[:6])
print(tuple1[: 5: -1])
for i in range(6):
        print(tuple1[i])
for i in tuple1:
        print(i)
D = {"apple":1}

