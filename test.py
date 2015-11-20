# -*- coding:utf-8 -*-
__author__ = 'HeYongxing'

import numpy as np

from util.getData import *
from regression.standRegression import *

# 十号线路
getData = getData()

data = getData.get_train_data(min_day="20140801", max_day="20141130", line_num=[10])
train = np.array(data)
xtrain = train[:, 0:-2]
ytrain = train[:, -1]

data = getData.get_train_data(min_day="20141201", max_day="20141207", line_num=[10])
test = np.array(data)
xtest = test[:, 0:-2]
ytest = test[:, -1]


from sklearn import linear_model
clf = linear_model.BayesianRidge(normalize=True)
clf.fit (xtrain, ytrain)
yHat = clf.predict(xtest)
print rssError(ytest, yHat)," BayesianRidge"

from sklearn import tree
clf = tree.DecisionTreeRegressor()
clf.fit (xtrain, ytrain)
yHat = clf.predict(xtest)
print rssError(ytest, yHat)," DecisionTreeRegressor"

from sklearn.ensemble import GradientBoostingRegressor

clf = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1,
     max_depth=1, random_state=0, loss='ls').fit(xtrain, ytrain)
yHat = clf.predict(xtest)
print rssError(ytest, yHat)," GradientBoostingRegressor"

from sklearn import kernel_ridge

clf = kernel_ridge.KernelRidge(kernel="rbf")
clf.fit(xtrain, ytrain)
yHat = clf.predict(xtest)
print rssError(ytest, yHat)," KernelRidge"

from sklearn.neighbors import KNeighborsRegressor
clf = KNeighborsRegressor(n_neighbors=1)
clf.fit(xtrain, ytrain)
yHat = clf.predict(xtest)
print rssError(ytest, yHat), " KNeighborsRegressor"


clf = linear_model.LassoLars(alpha=.01,normalize=True)
clf.fit(xtrain, ytrain)
yHat = clf.predict(xtest)
print rssError(ytest, yHat), " LassoLars"

