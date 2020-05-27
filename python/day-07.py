#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/27 上午10:08
# @Author  : huanghe
# @Site    : 
# @File    : day-07.py
# @Software: PyCharm
""":arg
直接手写一个 Python 类

直接手写一个构造函数

紧接着上面的代码，直接手写，补充完整代码，要求：

对列表中的人进行排序，并筛选出分数大于80的人的名单，组成一个新的列表显示出来。
代码如下：

class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age


class Student(Person):
    def __init__(self, name, gender, age,score):
        super(Student, self).__init__(name, gender, age)
        self.score = score

People = [kathy, Jim, John, Alice, Leo]
"""
class Person():
    def __init__(self, name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def show(self):
        print(self.name+self.age+self.gender)
        
class Student(Person):
    def set_age(self):
        self.age = '18'

class Teacher(Person):
    def __init__(self, name,age,gender,clsss):
        super(Teacher, self).__init__(name, age, gender)
        self.clsss = clsss
    def show(self):
        print(self.clsss)

        
# if __name__ == '__main__':
#     tom = Person(name='xiaoming', age='18',gender='male')
#     tom.show()
#     jerry = Teacher(name='xiaobai',age='20',gender='female',clsss='1')
#     jerry.show()
#     mike = Student(name='mike',age='17',gender='male')
#     mike.set_age()
#     mike.show()
""""""

# Python 的高阶函数有哪些，分别都有什么作用？

#map(function, sequence)
def is_obb(data):
    if data % 2 == 0:
        return data

def add_data(a,b):
    return a+b

    
print(list(map(is_obb,[1,2,3,4])))
print(list(filter(is_obb,[1,2,3,4])))

from functools import reduce
print(reduce(add_data, [1,2,3,4]))
        
    
#filter(function, iterable)
#reduce(function, sequence)
# 
# 简单说说生成器，迭代器，装饰器是什么，都有哪些作用？

#生成器:
#一边计算，一边返回
#(x for x in range(10))
g = (x for x in range(10))
print(next(g))

def getNum():
    for i in range(10):
        yield i

n =getNum()
print(n.__next__())

#迭代器
#拥有__iter__方法和__next__方法的对象
a = [1,2,3,4]
print(dir(g))

#装饰器
#本质是闭包函数
def func(fn):
    def func_in(*args, **kwargs):
        print("记录日志")
        print('访问方法'+fn.__name__)
        xx = fn(*args, **kwargs)
        return xx

    return func_in
@func
def test1():
    print("test1")

test1()



# 
# Python 中，如何将字符串转化为整型？
def to_int(str):
    try:
        int(str)
        return int(str)
    except ValueError: #报类型错误，说明不是整型的
        try:
            float(str) #用这个来验证，是不是浮点字符串
            return int(float(str))
        except ValueError:  #如果报错，说明即不是浮点，也不是int字符串。   是一个真正的字符串
            return False
        
a = to_int('aa')
print(a)
#
# 
# TCP 三次握手和四次挥手，请分别直接写出来
#三次握手：第一次  客户端给服务发条消息--》客户端发送能力OK  第二次：服务端收到消息并发出 --》服务端知道客户端发送能力ok；服务端接收能力OK，发送能力也OK
#第三次  客户端接收到消息，客户端知道了服务端发送与接收都ok  客户端接收能力OK  ===》可以进行通信了

#四次挥手
#第一次：客户端向服务器端发送 我要断开连接了   服务端收到客户端的释放请求向客户端发出连接释放的应答---客户端向服务的链接已断开  服务端不再接服务端的数据
#服务端数据发送完成后，向客户端发出连接断开的请求     客户端收到请求--发出确认应答
# 
# HTTP 常见的状态码有哪些？都是什么含义？
#200 - 请求成功
#301 - 资源（网页等）被永久转移到其它URL
#404 - 请求的资源（网页等）不存在
#500 - 内部服务器错误
# 
# webdriver 的核心原理是什么？
# cs模式  webdriver是一个协议，
#WebDriver 启动目标浏览器，并绑定到指定端口。该启动的浏览器实例，做为 web driver 的 remoteserver。
#Client 端通过 CommandExcuter 发送 HTTPRequest 给 remote server 的侦听端口（通信协议： thewebriver wire protocol）
#Remote server 需要依赖原生的浏览器组件（如：IEDriverServer.exe、chromedriver.exe），来转化转化浏览器的 native 调用。

# Appium 是什么？主要用来做什么的？它的核心原理是什么？
# 自动化开源测试工具   移动端自动化
# selenium1 和 selenium2 的区别是什么，为何要抛弃 selenium1? 它有什么缺陷？
#selenium1 js注入的方式  selenium2  浏览器原生API
# 常见的元素定位方法有哪些？
# ID name class_name link_text xpath css_selector
# 直接手写一个冒泡排序和快速排序，时间复杂度是多少？空间复杂度是多少？是否稳定？
#

def pop_sorted(data):
    for i in range(len(data)-1):
        for j in range(len(data)-i-1):
            if data[j+1] < data[j]:
                data[j],data[j+1] = data[j+1],data[j]
    return data
    
print(pop_sorted([1,3,2,4,7,5]))

def quick_sorted(data):
    if len(data) <2:
        return data
    base_data = data[0]
    min_data = []
    max_data = []
    data.pop(0)
    for item in data:
        if item < base_data:
            min_data.append(item)
        else:
            max_data.append(item)

    return quick_sorted(min_data)+[base_data]+quick_sorted(max_data)

    
print(quick_sorted([3,1,2,5,4]))
    


# 如何查询 Linux 后台日志，直接写出命令
# tail -f -n 200 /app/app.log
# 如何查看当前进程？
# top
#top -H -p 327
# Dockerfile 是什么？如何去创建一个 Dockerfile？
# docker image 构建文件
# Python 有没有垃圾回收机制？它又是通过什么来的？
# 有
# 熟悉 TestNG？那请说一下用法？
# 
# 熟悉 Java，那请直接手写一个单例模式？
# 
# 数据库增删改查，手写 SQL
# 
# Redis 是做什么用的？ElasticSearch是什么？做什么用的？
# 
# 接口测试怎么做的？如果存在接口依赖关系，怎么做？
# 
# 元组和列表的区别是什么？
# 
# Python中，*arg 和 *kwarg 分别代表什么含义，都有哪些作用？
# 
# 写过爬虫吗？那请说一下常见的反爬机制有哪些？如果是动态加载的页面，看不到数据，如何去进行爬取？

