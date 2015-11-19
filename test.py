# -*- coding:utf-8 -*-
__author__ = 'HeYongxing'

from items import *
from util.dbutil import dbutil
from util.string2num import string2num
from sqlalchemy import func
import datetime

w = weather()
s2num = string2num()
session = dbutil().get_session()
gd = session.query(gd_train.Deal_time, func.count(gd_train.Deal_time)).group_by(gd_train.Deal_time).all()

weathers = session.query(weather).all()
print len(weathers[0].Weather_day)
weathers = {datetime.datetime.strftime(tem.Date_time, "%Y%m%d"):
            [tem.Date_time.isoweekday(),
             s2num.weather2num(tem.Weather_day),
             tem.Temperature_max,
             tem.Temperature_min]
            for tem in weathers}
data = []
for tem in gd:
    i = [tem[1],tem[0].hour]
    data.append(i.extend(weather[datetime.datetime.strftime(tem[0], "%Y%m%d")]))



import numpy as np

data = np.array(data)