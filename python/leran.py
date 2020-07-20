#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/22 下午2:49
# @Author  : huanghe
# @Site    : 
# @File    : leran.py
# @Software: PyCharm

def pop_sorted(data):
    if len(data)<2:
        return data

    for i in range(len(data)-1):
        for j in range(len(data)-i-1):
            if data[j] > data[j+1]:
                data[j],data[j+1] = data[j+1],data[j]
    return data

'''
2.一个数组 找出三个数相加为0的数
a=[-2,3,5,0,-1,2,1]

求结果：
aa=[-2,0,2],[-1,0,1]'''

def add_zero(data):
    now_data = data
    result_data = []
    for i in now_data:
        mid_data =[]
        for m in now_data:
            mid_data.append(m)
        mid_data.remove(i)
        for j in mid_data:
            mid_data.remove(j)
            for k in mid_data:
                sum = i+j+k
                if sum == 0:
                    param = sorted([i,j,k])
                    if param not in result_data:
                        result_data.append(param)

    return result_data














if __name__ == '__main__':
    a = [-2, 3, 5, 0, -1, 2, 1]
    data = add_zero(a)
    print(data)

