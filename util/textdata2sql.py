# -*- coding:utf-8 -*-
__author__ = 'HeYongxing'
import time

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from items import *

engine = create_engine('mysql+mysqlconnector://root@localhost:3306/tianchi')
DBSession = sessionmaker(bind=engine)
session = DBSession()

# 线路6,14,广州市内

import codecs,re

# # 线路数据存入数据库
# with codecs.open("./data/gd_line_desc.txt",encoding="utf-8") as f:
#     while 1:
#         lines = f.readlines(10000)
#         if not lines:
#             break
#         for line in lines:
#             tem = line.split(",")
#             g_line = gd_line()
#             g_line.Line_name = tem[0]
#             g_line.Stop_cnt = int(tem[1])
#             g_line.Line_type = tem[2]
#             session.add(g_line)
#         session.commit()

# 训练数据存入数据库
_ = 0
start = time.time()
with codecs.open("/Users/lioo/Desktop/tianchi/part2/gd_train_data.txt",encoding="utf-8") as f:
    while 1:
        line = f.readline()
        _ +=1

        if not line:
            break

        # session.execute(
        #     gd_train.__table__.insert(),
        #     [{'Use_city': line.split(",")[0],'Line_name': line.split(",")[1],
        #       'Terminal_id': line.split(",")[2],'Card_id': line.split(",")[3],
        #       'Create_city': line.split(",")[4],'Deal_time': time.strptime(line.split(",")[5], "%Y%m%d%H"),
        #       'Cart_type': line.split(",")[6]}]
        # )
        # session.commit()

        tem = line.split(",")
        train = gd_train()
        train.Use_city = tem[0]
        train.Line_name = tem[1]
        train.Terminal_id = tem[2]
        train.Card_id = tem[3]
        train.Create_city = tem[4]
        train.Deal_time = time.strptime(tem[5], "%Y%m%d%H")
        train.Cart_type = tem[6]
        session.add(train)
        session.commit()
        if _%10000==0:
            print "the ", _/10000, "times, cost ", time.time() - start
            start = time.time()

# 天气数据存入数据库
# with codecs.open("./data/gd_weather_report.txt",encoding="utf-8") as f:
#     while 1:
#         lines = f.readlines(1000)
#         if not lines:
#             break
#         for i,line in enumerate(lines):
#             # 数据样例
#             # 2014/8/1,晴/雷阵雨,36℃/26℃,无持续风向≤3级/无持续风向≤3级
#             if i%2==1:
#                 continue
#
#             tem = line.split(",")
#             w = weather()
#             w.Date_time = time.strptime(tem[0], "%Y/%m/%d")
#             w.Weather_day = tem[1].split("/")[0]
#             w.Weather_night = tem[1].split("/")[1]
#             w.Temperature_max = re.findall("\d+",tem[2])[0]
#             w.Temperature_min = re.findall("\d+",tem[2])[1]
#             wind_day = tem[3].split("/")[0]
#             wind_night = tem[3].split("/")[1]
#             w.Wind_direction_day = re.findall(u"[\u4E00-\u9FA5]+",wind_day)[0] # 提取中文
#             w.Wind_direction_night = re.findall(u"[\u4E00-\u9FA5]+",wind_night)[0]
#             temperature = re.findall("\d+",wind_day)
#             w.Wind_force_max_day = int(temperature[-1])
#             w.Wind_force_min_day = 0
#             if len(temperature)>1:
#                 w.Wind_force_min_day = int(temperature[0])
#             temperature = re.findall("\d+",wind_night)
#             w.Wind_force_max_night = int(temperature[-1])
#             w.Wind_force_min_night = 0
#             if len(temperature)>1:
#                 w.Wind_force_min_night = int(temperature[0])
#             session.add(w)
#         session.commit()