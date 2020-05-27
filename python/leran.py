#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/22 下午2:49
# @Author  : huanghe
# @Site    : 
# @File    : leran.py
# @Software: PyCharm

def fun(*args, **kwargs):
    print(args)
    print(kwargs)



if __name__ == "__main__":
    fun(1,2,3,a=123)
