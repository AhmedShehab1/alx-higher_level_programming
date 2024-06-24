#!/usr/bin/python3
from model_state import Base, State
from sqlalchemy import create_engine
import sys

if __name__ == '__main__':
        engine = create_engine("mysql+mysqldb://ahmed:ahmedshehab@localhost/aspect", pool_pre_ping=True)

        Base.metadata.create_all(engine)

