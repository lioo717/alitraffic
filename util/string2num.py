# -*- coding:utf-8 -*-
__author__ = 'HeYongxing'

class string2num:

    @staticmethod
    def weather2num(s):
        data = {u"晴":1,
                u"多云":2,
                u"阴":3,
                u"阵雨":4,
                u"雷阵雨":5,
                u"小雨":6,
                u"小到中雨":7,
                u"霾":8,
                u"中雨":9,
                u"中到大雨":10,
                u"大雨":11,
                u"大到暴雨":12}

        return data[s]
    @staticmethod
    def line2num(s):
        data = {u"线路10":10, u"线路15":15}

        return data[s]