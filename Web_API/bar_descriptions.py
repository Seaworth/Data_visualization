#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@version: Python 3.6.3
@author: Seaworth
@software: PyCharm Community Edition
@file: bar_descriptions.py
@time: 2018/9/12 21:18
"""
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style=LS('#333366',base_style=LCS)
chart=pygal.Bar(style=my_style,x_label_rotation=45,show_legend=False)

chart.title='Python Projects'
chart.x_labels=['httpie','django','flask']

plot_dicts=[
    {'value':16101,'label':'Description of httpie'},
    {'value':15028,'label':'Description of django'},
    {'value':14879,'label':'Description of flask'},
]

chart.add("",plot_dicts)
chart.render_to_file('bar_description.svg')