#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@version: Python 3.6.3
@author: Seaworth
@software: PyCharm Community Edition
@file: americas.py
@time: 2018/9/10 20:59
"""
import pygal_maps_world.maps
wm=pygal_maps_world.maps.World()
wm.title="North, Center, and South America"

wm.add('North America',['ca','mx','us'])
wm.add('Center America', ['bz','cr','gt','hn','ni','pa','sv'])
wm.add('South America', ['ar','bo','br','cl','co','ec','gf',
                         'gy','pe','py','sr','uy','ve'])

wm.render_to_file('americas.svg')
