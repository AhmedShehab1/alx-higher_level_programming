#!/usr/bin/python3
"""
script that prints the first State object from db
"""
import sys
from sqlalchemy.orm import Session
from model_state import Base, State
from sqlalchemy import create_engine, select, text
if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    stmt = select(State).where(State.name == sys.argv[4])
    try:
        state_object = session.scalars(stmt).one()
        print(state_object.id)
    except Exception:
        print("Not found")
    finally:
        session.close()
