#!/usr/bin/python3
"""
Script that adds the State object Louisiana to the db
"""
import sys
from sqlalchemy.orm import Session
from model_state import Base, State
from sqlalchemy import create_engine
if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    new_state = State(name="Louisiana")
    session = Session(engine)
    session.add(new_state)
    session.commit()
    print(new_state.id)
    session.close()
