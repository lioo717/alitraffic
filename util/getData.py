# -*- coding:utf-8 -*-
__author__ = 'HeYongxing'

from datetime import datetime

from sqlalchemy import func

from items import *
from util.dbutil import dbutil
from util.string2num import string2num


class getData:
    def __init__(self):
        self.session = dbutil().get_session()
        [self.group_gd, self.weathers] = self.get_data()

    def get_data(self):
        """

        :return:[group_gd, weathers],
        """
        s2num = string2num()
        group_gd = self.session.query(gd_train.Deal_time, gd_train.Line_name, func.count(gd_train.Deal_time)).group_by(
            gd_train.Deal_time).group_by(gd_train.Line_name).all()
        weathers = self.session.query(weather).all()
        print type(weathers[2].Weather_day)
        weathers = [[datetime.strftime(tem.Date_time, "%Y%m%d"),  # 时间字符串
                     tem.Date_time,  # 时间
                     tem.Date_time.isoweekday(),  # 周几
                     s2num.weather2num(tem.Weather_day),  # 天气
                     tem.Temperature_max,  # 最高温
                     tem.Temperature_min]  # 最低温
                    for tem in weathers]
        group_gd = [[datetime.strftime(tem[0], "%Y%m%d"),  # 时间字符串
                     tem[0],  # 时间
                     tem[0].hour,  # 小时
                     s2num.line2num(tem[1]),  # 线路
                     tem[2]]  # 数量
                    for tem in group_gd]

        return [group_gd, weathers]

    def get_train_data(self, hour_range=range(6, 22), min_day="20140801", max_day="20141231",
                       line_num=[10, 15]):
        """
        返回的数据, 从min_day到max_day中每天时间在hour_range中的数据, 可以选择返回线路

        :param hour_range: 时间段
        :param min_day: 最小日期 "20140801"
        :param max_day: 最大日期
        :param line_num: 线路 (list)
        :return: data [星期, 天气, 最高温, 最低温, 小时, 线路, 数量(y)]
        """
        import copy

        [group_gd, weathers] = [self.group_gd, self.weathers]
        min_day = datetime.strptime(min_day, "%Y%m%d")
        max_day = datetime.strptime(max_day, "%Y%m%d")

        group_gd = [tem for tem in group_gd if ((tem[2] in hour_range) and tem[1] <= max_day and tem[1] >= min_day)]
        group_gd_date = [tem[0] for tem in group_gd]
        group_gd_data = [tem[2:] for tem in group_gd]
        weather_date = [tem[0] for tem in weathers if (tem[1] <= max_day and tem[1] >= min_day)]
        weather_data = [tem[2:] for tem in weathers if (tem[1] <= max_day and tem[1] >= min_day)]
        data = []
        for ind, tem in enumerate(group_gd_data):
            _ = None
            _ = copy.deepcopy(weather_data[weather_date.index(group_gd_date[ind])])
            _.extend(tem)
            data.append(_)

        data = [tem for tem in data if tem[-2] in line_num]

        return data

    def get_test_data(self):
        """
        :return: 返回20150101到20150107的测试数据集
                [[20150101, 4, 1, 19, 6, 6], ..., [20150107, 3, 2, 17, 10, 21]]
        """
        import copy
        weathers = self.weathers
        hour_range = range(6, 22)
        date = range(20150101, 20150108)
        weather_date = [tem[0] for tem in weathers]
        weather_data = [tem[2:] for tem in weathers]
        test = []
        for tem in date:
            tem_data = [tem,]
            tem_data.extend(weather_data[weather_date.index(str(tem))])
            for hour in hour_range:
                _ = copy.deepcopy(tem_data)
                _.append(hour)
                test.append(_)

        return test
