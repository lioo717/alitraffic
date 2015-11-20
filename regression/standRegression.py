# -*- coding:utf-8 -*-
#just to explain standard Regression
# feature = [ startdate week time weather_day]
# out = [peoplecnt]
# X.append(featuure)
# Y.append(out)
# yHat means the prediction ;yMat means the real value

from numpy import *
def standRegression(X, Y):
    xMat = mat(X)
    yMat = mat(Y).T
    xTx = xMat.T * xMat
    if linalg.det(xTx) ==0.0:
        print "Singular matrix cannot do reverse"
        return
    wx = xTx.T * (xMat.T*yMat)
    return wx

def predict(xMat, ws):
    yHat = xMat * ws
    return yHat


def rssError(yArr, yHatArr):
    return ((yArr - yHatArr)/yArr).sum()/yHatArr.size
