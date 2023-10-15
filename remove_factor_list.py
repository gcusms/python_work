#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :remove_factor_list.py
@时间        :2023/10/16 02:11:09
@邮箱        :2436210442@qq.com
@作者        :gcusms
@版本        :1.0
'''

# 移除列表当中的元素
list_1 = [1,12,53,64,32]
list_move = [1,64]

for i in list_move:
  list_1.remove(i)

print(list_1)

