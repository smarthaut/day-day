#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/28 下午4:35
# @Author  : huanghe
# @Site    : 
# @File    : aliyun-oss.py
# @Software: PyCharm
#LTAI4FyLtTzmpw2YTenwbJMp
#Y6JgsSh20K0tNSRD8doNysLkuo48z1
# import oss2
#
# auth = oss2.Auth('LTAI4FyLtTzmpw2YTenwbJMp','Y6JgsSh20K0tNSRD8doNysLkuo48z1')
# bucket = oss2.Bucket(auth,'oss-cn-beijing.aliyuncs.com','smarthe')
# object_names = 'users/local/aaa.txt'
# local_file = '/Users/huanghe/Desktop/aaa.txt'
# bucket.put_object_from_file(object_names, local_file)

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
client = AcsClient('LTAI4FfVu9cqTQi9Bfqa4YX9', '5HT4XO65JXugVwBYdmu6X1fEb28fEc', 'cn-hangzhou')

request = CommonRequest()
request.set_accept_format('json')
request.set_domain('dysmsapi.aliyuncs.com')
request.set_method('POST')
request.set_protocol_type('https') # https | http
request.set_version('2017-05-25')
request.set_action_name('SendSms')

request.add_query_param('RegionId', "cn-hangzhou")
request.add_query_param('PhoneNumbers', "13764302013")
request.add_query_param("SignName", "车吧云")
request.add_query_param("TemplateCode", "SMS_192830991")
name = "张三"
url = "ewewtype=3&agencyId=2"
request.add_query_param("TemplateParam", "{\"name\":\"" + name + "\", \"url\":\"" + url + "\"}")

response = client.do_action(request)
# python2:  print(response)
print(str(response, encoding = 'utf-8'))