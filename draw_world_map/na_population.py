#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@version: Python 3.6.3
@author: Seaworth
@software: PyCharm Community Edition
@file: na_population.py
@time: 2018/9/10 21:08
"""
import pygal_maps_world.maps
wm=pygal_maps_world.maps.World()
wm.title='Populations of Countries in North America'
wm.add('North America',{'ca':3412600,'us':309349000,'mx':113423000})

wm.render_to_file('na_population.svg')

