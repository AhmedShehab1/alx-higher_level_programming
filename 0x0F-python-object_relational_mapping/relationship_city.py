#!/usr/bin/python3
"""
Module Containing class definition of city and instance Base
"""
from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship, backref
from relationship_state import Base


class City(Base):
    """
    class definition of city
    Args:
        Base (class): inheriting from Base Class
    """
    __tablename__ = 'cities'
    id = Column(Integer(), primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer(), ForeignKey('states.id'), nullable=False)
    state = relationship('State', back_populates='cities')
