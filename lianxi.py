#!/usr/bin/python
# -*- coding: UTF-8 -*-

import seldom
from seldom.testdata import *
from seldom.har2case import utils
import uuid
import datetime
import json

# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
#
# 程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
#
# 程序源代码：

# for i in range(1, 5):
#     for j in range(1, 5):
#         for k in range(1, 5):
#             if (i != k) and (i != j) and (j != k):
#                 print(i, j, k)

# 题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按
# 10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可
# 提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，
# 求应发放奖金总数？
# 程序分析：请利用数轴来分界，定位。

# i = int(input('净利润:'))
# arr = [1000000, 600000, 400000, 200000, 100000, 0]
# rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
# r = 0
# for idx in range(0, 6):
#     if i>arr[idx]:
#         r+=(i-arr[idx])*rat[idx]
#         print ((i-arr[idx])*rat[idx])
#         i=arr[idx]
# print (r)

# day = get_ymd("Y").replace('-', '')
# day1 = get_date()
# year = get_year()
# m = get_month().replace(f'{get_year()}-', '')
# t = get_now_datetime(True)
# i = datetime.datetime.now()
# a = get_date(Type="%Y.%m.%d")
# b = get_ymd("m", -1).replace('-', '.')
# # d = "2023-02-22 13:08:31"
# dd = get_strftime(get_now_datetime(True), "%Y.%m.%d %H:%M")
#
# print(dd)

# dd = datetime.datetime.strptime(d, "%Y-%m-%d %H:%M:%S")
# dd = dd.strftime(t, "%Y-%m-%d")
# if a==dd:
#     print("123")
#
# print(dd)

# str1 = 'username=lisi&password=123456&address=中贸广场'
#
# dict1 = {}
#
# list1 = str1.split('&')#['username=lisi', 'password=123456', 'address=中贸广场'
# for x in list1:
#     list2= x.split('=')
#     dict1[list2[0]] = list2[1]
# print(dict1)


# body = 'appId=2fd5f092-d360-4783-b95c-6d47ee5cac44'
# body_ = str_to_dict(body)
# print(body_)
# c = get_date(1, "/")
# print(c)

# b = json.dumps(a, ensure_ascii=False)
# print(b)
t = "2023-03-06 17:37:39"
a = get_now_datetime()
b = a.strftime("%Y-%m-%d %H:%M:%S")



print(b)
