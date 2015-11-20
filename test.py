# -*- coding:utf-8 -*-
__author__ = 'HeYongxing'

from items import *
from util.dbutil import dbutil
from util.string2num import string2num
from sqlalchemy import func
import datetime


def get_data():
    """
    group_gd = [(Deal_time,count_of_deals))]
                 时段(datetime) ,客流量(int)
    weathers = {Date_time:[wday, weather_num, Temperature_max, Temperature_min]}
                时间(string,"20141001"):[一周的第几天(1-7), 天气数值(int), 最高温(int),最低温(int)]
    :return:[group_gd, weathers],
    """
    s2num = string2num()
    session = dbutil().get_session()
    group_gd = session.query(gd_train.Deal_time, func.count(gd_train.Deal_time)).group_by(gd_train.Deal_time).all()

    weathers = session.query(weather).all()
    print len(weathers[0].Weather_day)
    weathers = {datetime.datetime.strftime(tem.Date_time, "%Y%m%d"):
                [tem.Date_time.isoweekday(),
                 s2num.weather2num(tem.Weather_day),
                 tem.Temperature_max,
                 tem.Temperature_min]
                for tem in weathers}

    return [group_gd, weathers]

import numpy as np

[group_gd, weathers] = get_data()
# 构造数据集
# data = []
#
# data = [[tem[1],tem[0].hour, tem2 for tem2 in weathers[datetime.datetime.strftime(tem[0], "%Y%m%d")]] for tem in group_gd]
# xtrain = np.array(data[:,2:])