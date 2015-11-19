# -*- coding:utf-8 -*-
__author__ = 'HeYongxing'
from sqlalchemy import Column, Integer, VARCHAR, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class gd_line(Base):
    # 表的名字:
    __tablename__ = 'gd_line'

    # 表的结构:
    Line_name = Column(VARCHAR(20), primary_key=True)
    Stop_cnt = Column(Integer)
    Line_type = Column(VARCHAR(45))


class gd_train(Base):
    # 表的名字:
    __tablename__ = 'gd_train'

    # 表的结构:
    id = Column(Integer, primary_key=True, autoincrement=True)
    Use_city = Column(VARCHAR(45))
    Line_name = Column(VARCHAR(45))
    Terminal_id = Column(VARCHAR(45))
    Card_id = Column(VARCHAR(45))
    Create_city = Column(VARCHAR(45))
    Deal_time = Column(DateTime)
    Cart_type = Column(VARCHAR(45))


class weather(Base):
    # 表的名字:
    __tablename__ = 'weather'

    # 表的结构:
    id = Column(Integer, primary_key=True, autoincrement=True)
    Date_time = Column(DateTime)
    Weather_day = Column(VARCHAR(45))
    Weather_night = Column(VARCHAR(45))
    Temperature_max = Column(Integer)
    Temperature_min = Column(Integer)
    Wind_direction_day = Column(VARCHAR(45))
    Wind_direction_night = Column(VARCHAR(45))
    Wind_force_max_day = Column(Integer)
    Wind_force_min_day = Column(Integer)
    Wind_force_max_night = Column(Integer)
    Wind_force_min_night = Column(Integer)
