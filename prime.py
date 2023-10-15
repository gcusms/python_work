#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :main.py
@时间        :2023/10/15 23:43:27
@邮箱        :2436210442@qq.com
@作者        :gcusms
@版本        :1.0
'''
# 求区间内所有的素数
# 

import numpy as np



def input_number(n):
  if n <= 1:
    return False
  for i in range(2,n):
    print(i)
    if n % i == 0:
      print(n)
      return False
  return True

print(input_number(12))