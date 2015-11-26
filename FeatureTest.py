# -*- coding:utf-8 -*-
__author__ = 'HeYongxing'

import numpy as np
from matplotlib.pylab import show
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from util.getData import *


# 十号线路
# [星期, 天气, 最高温, 最低温, 小时, 线路, 数量(y), datetime]
getData = getData()

data = getData.get_train_data(min_day="20140901", max_day="20141231", line_num=[15])
train = np.array(data)
xtrain = train[:, 0:-3]
xdate = train[:, -1]
ytrain = train[:, -2]

# fig = figure()
# ax1 = fig.add_subplot(1, 1, 1)
# ax1.scatter(xtrain[:, 0], ytrain, c='red',
#             alpha=0.3, edgecolors='none')
# ax1.set_xlabel(u'星期')
# ax1.grid(True)
# show()
#

#
# fig = figure()
# ax1 = fig.add_subplot(1, 1, 1)
# ax1.scatter(xtrain[:, 2], ytrain, c='red',
#             alpha=0.3, edgecolors='none')
# ax1.set_xlabel(u'最高温')
# ax1.grid(True)
# show()
#
# fig = figure()
# ax1 = fig.add_subplot(1, 1, 1)
# ax1.scatter(xtrain[:, 3], ytrain, c='red',
#             alpha=0.3, edgecolors='none')
# ax1.set_xlabel(u'最低温')
# ax1.grid(True)
# show()
#
# fig = figure()
# ax1 = fig.add_subplot(1, 1, 1)
# ax1.scatter(xtrain[:, 4], ytrain, c='red',
#             alpha=0.3, edgecolors='none')
# ax1.set_xlabel(u'小时')
# ax1.grid(True)
# show()

# fig = figure()
# ax1 = fig.add_subplot(1, 1, 1)
# ax1.scatter(xdate, ytrain, c='red',
#             alpha=0.3, edgecolors='none')
# ax1.set_xlabel(u'时间')
# ax1.grid(True)
# show()

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')
ax1.scatter(xtrain[:, 0], xtrain[:, 4], ytrain, c='blue', alpha=0.3, edgecolors='none')
ax1.set_xlabel(u'weekday')
ax1.set_ylabel(u'hour')
ax1.set_zlabel(u'volume')
ax1.grid(True)
show()
