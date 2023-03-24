#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    __tablename__ = 'cities'
    """ The city class, contains state ID and name """
    state_id = Column(String(128), nullable=False)
    name =  Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship('place', backref='cities', cascade='all, delete')
