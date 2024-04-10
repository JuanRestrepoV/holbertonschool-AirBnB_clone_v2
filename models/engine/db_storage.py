"""
Class DBStorage
"""


class DBStorage():
    __engine = None
    __session = None
    
    def __init__(self):
        self.__engine = 