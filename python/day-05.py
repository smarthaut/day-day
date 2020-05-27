#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/22 下午2:39
# @Author  : huanghe
# @Site    : 
# @File    : day-05.py
# @Software: PyCharm
"""
is和==的区别
Python中的对象包含三要素：id、type、value
is id
== value
print(1is 1.0) False
print(1== 1.0) True


简述Python的深浅拷贝以及应用场景？
浅拷贝指仅仅拷贝数据集合的第一层数据，深拷贝指拷贝数据集合的所有层


Python垃圾回收机制？


Python的可变类型和不可变类型？
可变：列表、字典  不可变：数字、字符串、元组
求结果：
    v = dict.fromkeys(['k1','k2'],[]) 
   v[‘k1’].append(666)
    print(v) 
   v[‘k1’] = 777
    print(v)
"""
import copy

a= {"k1":"v1","k2":"v2","k3":[1,2,3]}
b=a
c=copy.copy(a)
d=copy.deepcopy(a)


a["k4"] = "v4"
a["k3"] = [1,2]
print(b)
print(c)
print(d)

v = dict.fromkeys(['K1','K2'],[])
v['K1'].append(666)
print(v)
v['K1'] = 77
print(v)






