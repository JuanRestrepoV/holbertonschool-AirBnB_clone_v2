#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref="state", cascade="delete")

    @property
    def get_cities(self):
        cities_for_state = []
        for city in self.cities:
            if city.state_id == self.id:
                cities_for_state.append(city)
        return cities_for_state
