#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@version: Python 3.6.3
@author: Seaworth
@software: PyCharm Community Edition
@file: dice_visual.py
@time: 2018/9/6 15:16
"""
import pygal
from die import Die
# 创建一个D6
die_1=Die()
die_2=Die(10)# 10面的骰子

# 掷几次骰子，并将结果存储在一个列表中
results=[]
for roll_num in range(50000):
    result=die_1.roll()+die_2.roll()# 两个骰子之和为结果
    results.append(result)

# 分析结果
frequencies=[]
max_value=die_1.num_sides+die_2.num_sides+1
for value in range(1,max_value):
    frequency=results.count(value)# results中有多少个value
    frequencies.append(frequency)

print(frequencies)

# 对结果进行可视化
hist =pygal.Bar()

hist.title='Results of rolling a D6 and a D10 50,000 times'
hist.x_labels=['2','3','4','5','6','7','8','9','10','11','12',
               '13','14','15','16']
hist.x_title='Result'
hist.y_title='Frequency of Result'

hist.add('D6+D10',frequencies)
hist.render_to_file('dice_visual.svg')
