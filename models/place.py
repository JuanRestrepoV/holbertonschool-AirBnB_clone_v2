#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer

class Place(BaseModel):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), nullable=False, ForeignKey('cities.id'))
    user_id = Column(String(60), nullable=False, ForeignKey('users.id'))
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer(0), nullable=False)
    number_bathrooms = Column(Integer(0), nullable=False)
    max_guest = Column(Integer(0), nullable=False)
    price_by_night = Column(Integer(0), nullable=False)
    latitude = Column(Float()), nullable=False)
    longitude = Column(Float(0), nullable=False)
    amenity_ids = []
    
    reviews = Relationship('Review', backref="place", cascade="delete")
    
    @property
    def get_reviews(self):
        reviews_for_places = []
        for review in self.reviews:
            if review.place_id == self.id:
                reviews_for_places.append(review)
        return reviews_for_places
