#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@version: Python 3.6.3
@author: Seaworth
@software: PyCharm Community Edition
@file: countries.py
@time: 2018/9/10 20:33
"""
from pygal_maps_world.i18n import COUNTRIES


def get_country_code(country_name):
    """根据指定的国家，返回i18n使用的两个字母的国别码"""
    for code,name in COUNTRIES.items():
        if name==country_name:
            return code
    # 如果没有找到指定的国家，就返回None
    return None

# print(get_country_code('Andorra'))
# print(get_country_code('United Arab Emirates'))
# print(get_country_code('Afghanistan'))
# for country_code in sorted(COUNTRIES.keys()):
#     print(country_code,COUNTRIES[country_code])