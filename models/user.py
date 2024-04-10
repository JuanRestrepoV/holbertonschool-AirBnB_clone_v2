#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(String(128), Nullable=False)
    password = Column(String(128), Nullable=False)
    first_name = Column(String(128), Nullable=False)
    last_name = Column(String(128), Nullable=False)
