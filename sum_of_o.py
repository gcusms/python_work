#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :sum_of_o.py
@时间        :2023/10/16 02:07:03
@邮箱        :2436210442@qq.com
@作者        :gcusms
@版本        :1.0
'''


# 计算列表当中的偶数和

def number_add(n1,n2):
  result  = []
  for i in range(n1,n2+1):
    if i % 2 == 0:
      result.append(i)
  return result
  

n1 = 1
n2 = 10
print("%s到%s区间范围内的偶数是"%(n1,n2),number_add(n1,n2))