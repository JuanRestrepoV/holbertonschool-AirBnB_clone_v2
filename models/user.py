#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String


class User(BaseModel):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
<<<<<<< HEAD
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
=======
    email = Column(String(128), Nullable=False)
    password = Column(String(128), Nullable=False)
    first_name = Column(String(128), Nullable=False)
    last_name = Column(String(128), Nullable=False)
    places = Relationship('Place', backref="user", cascade="delete")
    reviews = Relationship('Review', backref="user", cascade="delete")
>>>>>>> b47846d (updating task 8 and 9)
