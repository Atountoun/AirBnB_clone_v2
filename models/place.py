#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship

from os import getenv


metadata = Base.metadata

place_amenity = Table(
        'place_amenity',
        metadata,
        Column(
            'place_id', String(60), ForeignKey(
                'places.id'), nullable=False, primary_key=True),
        Column(
            'amenity_id', String(60), ForeignKey(
                'amenities.id'), nullable=False, primary_key=True)
        )


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship(
                'Review', backref='place', cascade='all, delete')
        amenities = relationship(
                'Amenity', secondary='place_amenity', viewonly=False)
    else:
        @property
        def reviews(self):
            """Returns the list of Review instances with place_id equals
            to the current Place.id
            """
            from models import storage
            from models.review import Review

            reviews = []
            for review in storage.all(Review).values():
                if review.place_id == self.id:
                    reviews.append(review)
            return reviews

        @property
        def amenities(self):
            """Returns the list of Amenity instances based on the attribute
            amenity_ids that contains all Amenity.id linked to the Place
            """
            from models import storage
            from models.amenity import Amenity
            amenities_list = []
            for amenity in storage.all(Amenity).values():
                if amenity.id in self.amenty_ids:
                    amenities_list.append(amenity)
            return amenities_list

        @amenities.setter
        def amenities(self, amenity):
            """Setter attribute to add Amenity.id to amenity_ids"""
            from models.amenity import Amenity
            if isinstance(amenity, Amenity):
                self.amenity_ids.append(amenity.id)
