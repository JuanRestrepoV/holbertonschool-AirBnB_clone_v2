#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from models.review import Review

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'))
    user_id = Column(String(60), ForeignKey('users.id'))
    name = Column(String(128), nullable=False)
    description = Column(String(1024), default="NULL", nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float(0), nullable=True)
    longitude = Column(Float(0), nullable=True)
    amenity_ids = []

    reviews = relationship('Review', backref="place", cascade="delete")

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def get_reviews(self):
            from models.__init__ import storage
            reviews_for_places = []
            for review in storage.all(Review).values():
                if review.place_id == self.id:
                    reviews_for_places.append(review)
            return reviews_for_places
