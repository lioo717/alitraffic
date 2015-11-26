# -*- coding:utf-8 -*-
__author__ = 'HeYongxing'

from datetime import datetime, timedelta

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
                        0    1      2     3        4        5           6         7       8
        :return: data [星期, 天气, 最高温, 最低温, 节假日长度, 第i个节假日, 工作日长度, 第i个工作日, date,
                         9    10    11
                        小时, 线路, 数量(y)]
        """
        import copy

        [group_gd, weathers] = [self.group_gd, self.weathers]
        work_holiday = self.get_day_type(min_day, max_day)

        min_day = datetime.strptime(min_day, "%Y%m%d")
        max_day = datetime.strptime(max_day, "%Y%m%d")

        group_gd = [tem for tem in group_gd if ((tem[2] in hour_range) and tem[1] <= max_day and tem[1] >= min_day)]
        group_gd_date = [tem[0] for tem in group_gd]
        group_gd_data = [tem[2:] for tem in group_gd]
        weather_date = [tem[0] for tem in weathers if (tem[1] <= max_day and tem[1] >= min_day)]
        weather_data = [tem[2:] for tem in weathers if (tem[1] <= max_day and tem[1] >= min_day)]
        data = []

        for ind, tem in enumerate(group_gd_data):
            if tem[-2] in line_num:
                _ = None
                _ = copy.deepcopy(weather_data[weather_date.index(group_gd_date[ind])])
                _.extend(work_holiday[weather_date.index(group_gd_date[ind])])
                _.append(group_gd[ind][1])
                _.extend(tem)
                data.append(_)

        return data

    def get_test_data(self):
        """
        :return: 返回20150101到20150107的测试数据集
                    0    1    2     3     4        5         6         7        8          9
                 [日期, 星期, 天气, 最高温, 最低温, 节假日长度, 第i个节假日, 工作日长度, 第i个工作日, 小时]

        """
        import copy
        weathers = self.weathers
        hour_range = range(6, 22)
        date = range(20150101, 20150108)
        weather_date = [tem[0] for tem in weathers]
        weather_data = [tem[2:] for tem in weathers]
        work_holiday = self.get_day_type(min_day="20150101", max_day="20150107")
        test = []
        for ind, tem in enumerate(date):
            tem_data = [tem, ]
            tem_data.extend(weather_data[weather_date.index(str(tem))])
            tem_data.extend(work_holiday[ind])
            for hour in hour_range:
                _ = copy.deepcopy(tem_data)
                _.append(hour)
                test.append(_)
        return test

    def get_day_type(self, min_day="20140801", max_day="201517"):
        """分别是每天对应的节假日长度, 第i个节假日, 工作日长度, 第i个工作日, 例如10月3日,对应的为[7, 3, 0, 0]

        :param min_day: 开始日期
        :param max_day: 结束日期
        :return: [holidays, ith_holidays, workdays, ith_workdays] 分别是每天对应的节假日长度, 第i个节假日, 工作日长度, 第i个工作日
        """
        modified_holidays = ['20140906', '20140907', '20140908',
                             '20141001', '20141002', '20141003', '20141004', '20141005', '20141006', '20141007',
                             '20150101', '20150102', '20150103']
        modified_holidays = [datetime.strptime(tem, "%Y%m%d") for tem in modified_holidays]
        modified_workdays = ['20140928', '20141011',
                             '20150104']
        modified_workdays = [datetime.strptime(tem, "%Y%m%d") for tem in modified_workdays]

        min_day = datetime.strptime(min_day, "%Y%m%d")
        max_day = datetime.strptime(max_day, "%Y%m%d")

        oneday = timedelta(days=1)

        start_day = min_day + timedelta(days=-7)
        end_day = max_day + timedelta(days=7)

        i = 0
        daytype = [None] * ((end_day - start_day).days + 1)
        days = [None] * ((end_day - start_day).days + 1)
        tem_day = start_day
        while 1:
            if tem_day > end_day:
                break
            if tem_day.isoweekday() in range(1, 6):
                daytype[i] = 1
            if tem_day.isoweekday() in range(6, 8):
                daytype[i] = 0
            if tem_day in modified_workdays:
                daytype[i] = 1
            if tem_day in modified_holidays:
                daytype[i] = 0
            days[i] = tem_day
            i += 1
            tem_day = tem_day + oneday
        datelength = []
        dateind = []
        k = 0
        for ind, tem in enumerate(daytype):
            if ind == len(days) - 1:
                break
            if daytype[ind] == daytype[ind + 1]:
                k += 1
                dateind.append(k)
            else:
                k += 1
                dateind.append(k)
                datelength.extend([k for i in range(0, k)])
                k = 0
        tem_day = min_day
        holidays = []
        ith_holidays = []
        workdays = []
        ith_workdays = []
        while 1:
            if tem_day > max_day:
                break
            ind = days.index(tem_day)
            if daytype[ind]:
                holidays.append(0)
                ith_holidays.append(0)
                workdays.append(datelength[ind])
                ith_workdays.append(dateind[ind])
            else:
                holidays.append(datelength[ind])
                ith_holidays.append(dateind[ind])
                workdays.append(0)
                ith_workdays.append(0)
            tem_day = tem_day + oneday
            result = []
        for ind in range(0, len(holidays)):
            _ = [holidays[ind], ith_holidays[ind], workdays[ind], ith_workdays[ind]]
            result.append(_)
        return result
