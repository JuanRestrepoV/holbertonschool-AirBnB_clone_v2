#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Amenity(BaseModel):
    name = ""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship
