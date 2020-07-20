#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/29 下午2:46
# @Author  : huanghe
# @Site    : 
# @File    : day-08.py
# @Software: PyCharm
#
# 如何安装第三方模块？以及用过哪些第三方模块？
#
# 至少列举8个常用模块都有那些？
#
# re的match和search区别？
#
# 什么是正则的贪婪匹配？
#
# 求结果：  a. [ i % 2 for i in range(10) ]  b. ( i % 2 for i in range(10) )
#
# 求结果：  a. 1 or 2  b. 1 and 2  c. 1 < (2==2)  d. 1 < 2 == 2
#
# def func(a,b=[]) 这种写法有什么坑？

#包管理工具我用的是pip  requests pymysql selenium json yaml logging os datetime

import re
#match  从首位开始匹配
print(re.match('super','superman'))
print(re.match('super','asuper'))

#search
print(re.search('super','superman'))
print(re.search('super','asuper'))

print([ i % 2 for i in range(10) ])
print(list((i % 2 for i in range(10))))


print(1 or 2)
print(1  and 2)
print(1 < (2==2))
print(2 == 2)
print(1 < 2 == 2)

