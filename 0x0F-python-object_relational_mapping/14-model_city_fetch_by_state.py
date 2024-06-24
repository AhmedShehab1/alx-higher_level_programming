#!/usr/bin/python3
"""
Script that prints all cities objects from the db
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    for city in session.query(City).order_by(City.id).all():
        print(f"{city.state.name}: ({city.id}) {city.name}")
    session.close()
