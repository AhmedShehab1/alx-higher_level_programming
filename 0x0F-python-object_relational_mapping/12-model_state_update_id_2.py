#!/usr/bin/python3
"""
Script that Change the name of a State object in the db
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
    stmt = select(State).where(State.id == 2)
    session = Session(engine)
    state_2 = session.scalars(stmt).one()
    state_2.name = "New Mexico"
    session.commit()
    session.close()
