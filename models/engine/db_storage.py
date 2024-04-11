#!/usr/bin/python3
"""
Class DBStorage
"""
import os
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

clases = [User, State, City, Amenity, Place, Review]


class DBStorage():
    __engine = None
    __session = None

    def __init__(self):
        mysql_user = os.getenv("HBNB_MYSQL_USER")
        mysql_pass = os.getenv("HBNB_MYSQL_PWD")
        mysql_host = os.getenv("HBNB_MYSQL_HOST", default='localhost')
        mysql_db = os.getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine(
            f"mysql+mysqldb://{mysql_user}:{mysql_pass}@{mysql_host}/{mysql_db}", pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        newDict = {}
        # if cls is None:
        #     obj = self.__session.query(cls).all()
        #     for objs in obj:
        #         key = f"{obj.__class.__name}.{obj.id}"
        #         newDict[key] = objs
        #     print(newDict)
        return {}

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj != None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
