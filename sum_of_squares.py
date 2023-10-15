#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :sum_of_squares.py
@时间        :2023/10/16 00:55:46
@邮箱        :2436210442@qq.com
@作者        :gcusms
@版本        :1.0
'''
# 求前 n 项系数和

def sum_number(n):
  # result = 0
  # for i in range(1,n+1):
  #   result += i * i
  # return result
  return n * (n+1) * (2*n+1) / 6 # 纯数学计算公式


print(sum_number(2))