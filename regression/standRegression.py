# -*- coding:utf-8 -*-
# just to explain standard Regression
# feature = [ startdate week time weather_day]
# out = [peoplecnt]
# X.append(featuure)
# Y.append(out)
# yHat means the prediction ;yMat means the real value

import numpy as np


def rssError(yArr, yHatArr):
    a = abs(yArr - yHatArr) / yArr
    # 线性
    tem = (a-0.3) / (-3) * 10
    # e
    # tem = np.log((a+0.7).tolist())/np.log(0.7)
    tem = tem * (tem > 0)
    return tem.sum() / tem.size