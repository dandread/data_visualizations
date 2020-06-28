#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 12:29:26 2020

@author: dominickdandrea
"""


import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=20)

#Set chart title and label axes/
ax.set_title("Square Numbers", fontsize=24, pad=20)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Square of Values", fontsize=14)

#Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

#Set the range for and format each axis.
ax.axis([0,1000, 1, 1100000])
ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
ax.get_xaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

plt.show()