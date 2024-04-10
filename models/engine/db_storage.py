#!/usr/bin/python3
"""
Class DBStorage
"""
from MySQLdb import _mysql


class DBStorage():
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = _mysql.connect(user="hbnb_dev", db="hbnb_dev_db")
