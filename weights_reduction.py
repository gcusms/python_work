#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :weights_reduction.py
@时间        :2023/10/16 02:14:24
@邮箱        :2436210442@qq.com
@作者        :gcusms
@版本        :1.0
'''

# 元素去重

list_1 = [10,20,10,20,30,50,53,64]
# print(set(list_1)) # 可以去重，但是不是按照原来的顺序进行判断 {64, 10, 50, 20, 53, 30}

ult = []
# 方法二
for i in list_1:
  if i not in ult:
    ult.append(i)

print(ult) # 此方法可以按照原来列表顺序进行判断[10, 20, 30, 50, 53, 64]