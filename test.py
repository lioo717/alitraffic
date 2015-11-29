# -*- coding:utf-8 -*-
__author__ = 'HeYongxing'

from util.getData import *
from regression.standRegression import *

# 十号线路

getData = getData()


#                 0    1      2     3        4        5           6         7       8
# :return: data [星期, 天气, 最高温, 最低温, 节假日长度, 第i个节假日, 工作日长度, 第i个工作日, date,
#                  9    10    11
#                 小时, 线路, 数量(y)]

# :return: 返回20150101到20150107的测试数据集
#             0    1    2     3     4        5         6         7        8          9
#          [日期, 星期, 天气, 最高温, 最低温, 节假日长度, 第i个节假日, 工作日长度, 第i个工作日, 小时]

def test(min_day_train, max_day_train, min_day_test, max_day_test, line_num=[11], features=[0, 1, 2, 3, 4, 5, 6, 7, 9]):
    print " ", min_day_train, \
        " ", max_day_train, \
        " ", min_day_test, \
        " ", max_day_test, \
        " ", line_num[0],

    data = getData.get_train_data(min_day=min_day_train, max_day=max_day_train, line_num=line_num)
    train = np.array(data)

    xtrain = train[:, features]
    ytrain = train[:, -1]

    # data = getData.get_test_data()
    # test = np.array(data)
    # xtest = test[:, 1:]

    data = getData.get_train_data(min_day=min_day_test, max_day=max_day_test, line_num=line_num)
    test = np.array(data)
    xtest = test[:, features]
    ytest = test[:, -1]

    from sklearn import linear_model
    clf = linear_model.BayesianRidge(normalize=True)
    clf.fit(xtrain, ytrain)
    yHat = clf.predict(xtest)
    print  " ",rssError(ytest, yHat),

    from sklearn import tree
    clf = tree.DecisionTreeRegressor()
    clf.fit(xtrain, ytrain)
    yHat = clf.predict(xtest)
    print " ",rssError(ytest, yHat),

    from sklearn.ensemble import GradientBoostingRegressor

    clf = GradientBoostingRegressor()
    clf.fit(xtrain, ytrain)
    yHat = clf.predict(xtest)

    print  " ",rssError(ytest, yHat),

    from sklearn.neighbors import KNeighborsRegressor
    clf = KNeighborsRegressor(n_neighbors=1)
    clf.fit(xtrain, ytrain)
    yHat = clf.predict(xtest)

    print  " ",rssError(ytest, yHat),

    clf = linear_model.LassoLars(alpha=.01, normalize=True)
    clf.fit(xtrain, ytrain)
    yHat = clf.predict(xtest)
    print  " ",rssError(ytest, yHat)



test(min_day_train="20141010", max_day_train="20141120", min_day_test="20141001", max_day_test="20141007",
     line_num=[11])
test(min_day_train="20141010", max_day_train="20141120", min_day_test="20141001", max_day_test="20141007",
     line_num=[11], features=[0, 1, 4, 5, 6, 7, 9])
test(min_day_train="20141010", max_day_train="20141120", min_day_test="20141001", max_day_test="20141007",
     line_num=[11], features=[0, 1, 9])
test(min_day_train="20141010", max_day_train="20141120", min_day_test="20141001", max_day_test="20141007",
     line_num=[11], features=[0, 1, 2, 3, 9])
test(min_day_train="20141010", max_day_train="20141120", min_day_test="20141001", max_day_test="20141007",
     line_num=[11], features=[0, 1, 4, 6, 9])
test(min_day_train="20141010", max_day_train="20141120", min_day_test="20141001", max_day_test="20141007",
     line_num=[11], features=[0, 1, 5, 7, 9])
test(min_day_train="20141010", max_day_train="20141120", min_day_test="20141001", max_day_test="20141007",
     line_num=[11], features=[0, 1, 2,3,5, 7, 9])
test(min_day_train="20141010", max_day_train="20141120", min_day_test="20141001", max_day_test="20141007",
     line_num=[11], features=[0,5, 7, 9])
test(min_day_train="20141010", max_day_train="20141120", min_day_test="20141001", max_day_test="20141007",
     line_num=[11], features=[1, 5, 7, 9])
test(min_day_train="20141010", max_day_train="20141120", min_day_test="20141001", max_day_test="20141007",
     line_num=[11], features=[1,2,3, 4, 5, 9])
test(min_day_train="20141010", max_day_train="20141120", min_day_test="20141001", max_day_test="20141007",
     line_num=[11], features=[1, 4, 5, 6, 9])

test(min_day_train="20141010", max_day_train="20141120", min_day_test="20141001", max_day_test="20141007", line_num=[6])
test(min_day_train="20141010", max_day_train="20141120", min_day_test="20141001", max_day_test="20141007", line_num=[6],
     features=[0, 1, 4, 5, 6, 7, 9])
test(min_day_train="20141010", max_day_train="20141120", min_day_test="20141001", max_day_test="20141007", line_num=[6],
     features=[0, 1, 9])
test(min_day_train="20141010", max_day_train="20141120", min_day_test="20141001", max_day_test="20141007", line_num=[6],
     features=[0, 1, 2, 3, 9])
test(min_day_train="20141010", max_day_train="20141120", min_day_test="20141001", max_day_test="20141007", line_num=[6],
     features=[0, 1, 4, 6, 9])
test(min_day_train="20141010", max_day_train="20141120", min_day_test="20141001", max_day_test="20141007", line_num=[6],
     features=[0, 1, 5, 7, 9])
test(min_day_train="20141010", max_day_train="20141120", min_day_test="20141001", max_day_test="20141007", line_num=[6],
     features=[0, 1,2,3, 5, 7, 9])
test(min_day_train="20141010", max_day_train="20141120", min_day_test="20141001", max_day_test="20141007", line_num=[6],
     features=[0,5, 7, 9])
test(min_day_train="20141010", max_day_train="20141120", min_day_test="20141001", max_day_test="20141007", line_num=[6],
     features=[1, 5, 7, 9])
test(min_day_train="20141010", max_day_train="20141120", min_day_test="20141001", max_day_test="20141007", line_num=[6],
     features=[1,2,3, 4, 5, 9])
test(min_day_train="20141010", max_day_train="20141120", min_day_test="20141001", max_day_test="20141007", line_num=[6],
     features=[1, 4, 5, 6, 9])

#                 0    1      2     3        4        5           6         7       8
# :return: data [星期, 天气, 最高温, 最低温, 节假日长度, 第i个节假日, 工作日长度, 第i个工作日, date,
#                  9    10    11
#                 小时, 线路, 数量(y)]