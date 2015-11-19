# -*- coding:utf-8 -*-
__author__ = 'HeYongxing'

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# 使用方法:
# http://pythoncentral.io/introductory-tutorial-python-sqlalchemy/

class dbutil:
    def __init__(self):
        engine = create_engine('mysql+mysqlconnector://root@localhost:3306/tianchi')
        DBSession = sessionmaker(bind=engine)
        self.session = DBSession()

    def get_session(self):
        return self.session


