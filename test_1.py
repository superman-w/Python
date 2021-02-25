#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test_1.py
# @Time      :2021/2/25 11:06
# @Author    :WLT

# 不用int将字符串转换成整数
a = '123456789'
a = a[::-1]
sum1 = 0
for i, j in enumerate(a):
    for k in range(10):
        if str(k) == j:
            sum1 = sum1 + k*10**i
print(sum1)
