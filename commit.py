# -*- coding:utf-8 -*-
import codecs

import numpy as np

from util.getData import *
from regression.standRegression import *

'''
train_data:xtrain
train_label:ytrain
test_data:xpred
test_time:date_time
'''

getdata = getData()

#                 0    1      2     3        4        5           6         7       8
# :return: data [星期, 天气, 最高温, 最低温, 节假日长度, 第i个节假日, 工作日长度, 第i个工作日, date,
#                  9    10    11
#                 小时, 线路, 数量(y)]

# :return: 返回20150101到20150107的测试数据集
#             0    1    2     3     4        5         6         7        8          9
#          [日期, 星期, 天气, 最高温, 最低温, 节假日长度, 第i个节假日, 工作日长度, 第i个工作日, 小时]
#
# """
features = [0, 1, 2, 3, 4, 5, 6, 7, 9]

data = getdata.get_train_data(min_day="20140820", max_day="20141231", line_num=[6])
train = np.array(data)

xtrain1 = train[:, features]
ytrain1 = train[:, -1]

data = getdata.get_train_data(min_day="20140820", max_day="20141231", line_num=[11])
train = np.array(data)
xtrain2 = train[:, features]
ytrain2 = train[:, -1]

data = getdata.get_test_data()
test = np.array(data)
xtest = test[:, 1:]

from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import BayesianRidge


def regression(regressor):
    clf = regressor()
    clf.fit(xtrain1, ytrain1)
    yHat1 = clf.predict(xtest)

    clf2 = regressor()
    clf2.fit(xtrain2, ytrain2)
    yHat2 = clf2.predict(xtest)
    return [yHat1, yHat2]


def commit(title, xtest, yHat1, yHat2):
    # 线路15,20150104,07,0
    date = xtest[:, 0].tolist()
    yHat_1 = yHat1.tolist()
    yHat_2 = yHat2.tolist()
    i = 0
    f = codecs.open(title, "w", "utf-8")
    for idx in date:
        r = u'线路6' + ',' + str(idx) + ',' + str(xtest[i][-1]) + ',' + str(int(yHat_1[i])) + '\n'
        i += 1
        f.write(r)
    i = 0
    for idx in date:
        r = u'线路11' + ',' + str(idx) + ',' + str(xtest[i][-1]) + ',' + str(int(yHat_2[i])) + '\n'
        i += 1
        f.write(r)
    f.close()
    print 'done'


import time

if __name__ == '__main__':
    [yHat1, yHat2] = regression(DecisionTreeRegressor)
    commit("result_tree_%d.txt" % int(time.time()), np.array(test), yHat1, yHat2)
    [yHat1, yHat2] = regression(BayesianRidge)
    commit("result_bayesian_%d.txt" % int(time.time()), np.array(test), yHat1, yHat2)
