#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = Relationship('Place', backref="cities", cascade="delete")
