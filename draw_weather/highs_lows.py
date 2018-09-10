#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@version: Python 3.6.3
@author: Seaworth
@software: PyCharm Community Edition
@file: highs_lows.py
@time: 2018/9/6 16:20
"""
import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename='death_valley_2014.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)

    for index,colum_header in enumerate(header_row):
        # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
        print(index,colum_header)

    dates,highs,lows=[],[],[]# 日期，最高气温，最低气温
    for row in reader:# 找出每天最高温度
        try:
            current_date=datetime.strptime(row[0],'%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date,'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    # 根据数据绘制图形
    fig=plt.figure(dpi=128,figsize=(10,6))
    plt.plot(dates,highs,c='red',alpha=0.5)# alpha指示颜色的透明度，0表示完全透明，1表示完全不透明
    plt.plot(dates, lows, c='blue',alpha=0.5)
    plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)# 填充两个y值之间的空间

    # 设置图形的格式
    plt.title('Daily high and low temperatures, 2014\nDeath Valley',fontsize=24)
    plt.xlabel('date',fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel('temperature(F)',fontsize=16)
    plt.tick_params(axis='both',which='major',labelsize=16)

    plt.show()