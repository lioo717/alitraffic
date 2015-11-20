# -*- coding:utf-8 -*-
__author__ = 'HeYongxing'

from items import *
from util.dbutil import dbutil
from util.string2num import string2num
from sqlalchemy import func
from datetime import datetime


def get_data():
    """
    group_gd = [(Deal_time,count_of_deals))]
                 时段(datetime) ,客流量(int)
    weathers = [Date_time, wday, weather_num, Temperature_max, Temperature_min]
                [时间(string,"20141001"),一周的第几天(1-7), 天气数值(int), 最高温(int),最低温(int)]
    :return:[group_gd, weathers],
    """
    s2num = string2num()
    session = dbutil().get_session()
    group_gd = session.query(gd_train.Deal_time, func.count(gd_train.Deal_time)).group_by(gd_train.Deal_time).all()

    weathers = session.query(weather).all()
    print len(weathers[0].Weather_day)
    weathers = [[datetime.strftime(tem.Date_time, "%Y%m%d"),
                tem.Date_time.isoweekday(),
                 s2num.weather2num(tem.Weather_day),
                 tem.Temperature_max,
                 tem.Temperature_min]
                for tem in weathers]
    group_gd =  [[datetime.strftime(tem[0], "%Y%m%d"),
                  tem[0].hour,
                  tem[1]]
                for tem in group_gd]
    return [group_gd, weathers]

import numpy as np

[group_gd, weathers] = get_data()
# 构造数据集

group_gd_date = [tem[0] for tem in group_gd]
group_gd_data = [tem[1:] for tem in group_gd]
weather_date = [tem[0] for tem in weathers]
weather_data = [tem[1:] for tem in weathers]
data = []
for ind,tem in enumerate(group_gd_data):
    tem.extend(weather_data[weather_date.index(group_gd_date[ind])])
    data.append(tem)

xtrain = np.array(data)
