#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/9 上午11:16
# @Author  : huanghe
# @Site    : 
# @File    : day-11.py
# @Software: PyCharm
#1 1-100 求和
#print(sum(range(0,100)))
#2 如何在一个函数修改全部变量
# a = 5
# def set_num():
#     global a
#     a = 6
#     print(a)
# set_num()
#3 列出5个标准库
# import os
# import sys
# import datetime
# import math
# import requests

# 4 字典如何删除key和合并
# a = {"name":"张三","age":"18"}
# b = {"name":"李四","age":"20"}
# del  a["name"]
# print(a)
# a.update(b)
# print(a)

# 5 列表去重
# a = [1,2,3,4,5,6,6,6,7,8,8]
# print(list(set(a)))

# 6 map [1,2,3] ---> [2,4,6]
# def obj(n):
#     return 2 * n
# print(list(map(obj,[1,2,3])))

# 7 生成随机整数 随机小数  指定数值
# import random
# def get_random_data(type):
#     if type == 1:
#         return random.randint(0,100)
#     if type ==2 :
#         return random.random()
#     else:
#         return random.uniform(1,2)
# print(get_random_data(type=3))

# 8 s = "ajldjlajfdijfddd" 去重 从小到大 输出 前4位
# s = "ajldjlajfdijfddd"
# print("".join(sorted(set(s))[0:4]))

# 9 字典 根据key从小到大排序

# s = {"name":"zs","age":18,"city":"深圳","tel":"17621100899"}
# s1 = {}
# for key in sorted(s.keys()):
#     s1[key] = s[key]
# print(s1)

# 10 a = "adsfjsdfbuaisdbasfadsfbwibfqwfasdfbswerdsfashbfhja" 统计每个字符出现的次数

# from collections import Counter
# a = "adsfjsdfbuaisdbasfadsfbwibfqwfasdfbswerdsfashbfhja"
# print(dict(Counter(a)))
# result = {}
# for data in a:
#     if data in result.keys():
#         result[data] = result[data]+1
#     else:
#         result[data] = 1
# print(result)

# 11
# a = "abc"
# b = "def"
# print(a.join(b))

# 12 单例模式
# import threading
#
# class Singleton(object):
#     _instance_lock = threading.Lock()
#
#     def __init__(self):
#         pass
#
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(Singleton,"_instance"):
#             with Singleton._instance_lock:
#                 if not hasattr(Singleton, "_instance"):
#                     Singleton._instance = object.__new__(cls)
#         return Singleton._instance

# 13 mysql 存储引擎

# innerDB  : 支持事务 支持行级锁及外键
# MyISAM   : 不支持事务 不支持行级锁及外键
# b+树

# 进程与线程
# 进程：
# 操作系统进行资源分配和调度的基本单位，多个进程之间相互独立
# 线程：
# CPU进行资源分配和调度的基本单位，一个进程下的线程共享资源





