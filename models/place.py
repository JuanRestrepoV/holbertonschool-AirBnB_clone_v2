#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, Table
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from models.review import Review


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', ForeignKey(
                          'places.id'), primary_key=True, nullable=False),
                      Column('amenity_id', ForeignKey(
                          'amenities.id'), primary_key=True, nullable=False),
                      extend_existing=True
                      )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable="False")
    user_id = Column(String(60), ForeignKey('users.id'),  nullable="False")
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float(0), nullable=True)
    longitude = Column(Float(0), nullable=True)
    amenity_ids = []
    reviews = relationship('Review', backref="place", cascade="delete")
    amenities = relationship(
        'Amenity', secondary='place_amenity', viewonly=False, overlaps='place_amenities')

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def get_reviews(self):
            from models.__init__ import storage
            return [review for review in storage.all(Review).values() if review.place_id == self.id]

        @property
        def get_amenities(self):
            from models.amenity import Amenity
            from models.__init__ import storage
            return [amenity for amenity in storage.all(
                Amenity).values() if amenity.id == self.amenity_ids]

        @get_amenities.setter
        def get_amenities(self, amenity):
            from models.amenity import Amenity
            if type(amenity) == Amenity:
                self.amenity_ids.append(amenity.id)
