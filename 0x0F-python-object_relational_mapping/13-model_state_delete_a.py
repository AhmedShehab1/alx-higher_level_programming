#!/usr/bin/python3
"""
Script that delete State objects containing 'a'
"""
import sys
from sqlalchemy.orm import Session
from model_state import Base, State
from sqlalchemy import create_engine, select
if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    stmt = select(State).where(State.name.like("%a%"))
    for state_with_a in session.scalars(stmt):
        session.delete(state_with_a)
    session.commit()
    session.close()
