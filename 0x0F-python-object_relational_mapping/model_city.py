#!/usr/bin/python3
"""
Module Containing class definition of city and instance Base
"""
from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship, backref
from model_state import Base


class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer(), primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer(), ForeignKey('states.id'), nullable=False)
    state = relationship('State', backref=backref('cities', order_by=id))
