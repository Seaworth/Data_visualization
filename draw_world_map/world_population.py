#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@version: Python 3.6.3
@author: Seaworth
@software: PyCharm Community Edition
@file: world_population.py
@time: 2018/9/10 20:20
"""
import json
import pygal_maps_world.maps
from countries import get_country_code
from pygal.style import LightColorizedStyle as LCS,RotateStyle as RS

# 将数据加载到一个列表中
filename='population_data.json'
with open(filename) as f:
    pop_data=json.load(f)

# 创建一个包含人口数量的字典
cc_populaitons={}
for pop_dict in pop_data:
    if pop_dict['Year']=='2010':
        country_name=pop_dict['Country Name']
        population=int(float(pop_dict['Value']))# 有些数据包含小数，需要先转换为浮点型，再转换为整型
        code=get_country_code(country_name)
        if code:
            cc_populaitons[code]=population

# 根据人口数量将所有国家分成三组
cc_pops_1,cc_pops_2,cc_pops_3={},{},{}
for cc,pop in cc_populaitons.items():
    if pop<10000000:
        cc_pops_1[cc]=pop
    elif pop<1000000000:
        cc_pops_2[cc]=pop
    else:
        cc_pops_3[cc]=pop

# 看看每组分别包含多少个国家
print(len(cc_pops_3),len(cc_pops_2),len(cc_pops_1))


wm_style=RS('#336699',base_style=LCS)
wm=pygal_maps_world.maps.World(style=wm_style)
wm.title='World Population in 2010, by Country'
wm.add('>1bn',cc_pops_3)
wm.add('10m-1bn',cc_pops_2)
wm.add('0-10m',cc_pops_1)


wm.render_to_file('world_population.svg')
