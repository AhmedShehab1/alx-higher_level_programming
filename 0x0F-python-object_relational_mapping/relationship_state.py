#!/usr/bin/python3
"""
Module Containing class definition of state and instance Base
"""
from sqlalchemy import String, Integer, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()


class State(Base):
    """
   class definition of state
    Args:
        Base (class): inheriting from Base Class
    """
    __tablename__ = 'states'
    id = Column(Integer(), primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', back_populates='state',
                          cascade='all, delete-orphan')
