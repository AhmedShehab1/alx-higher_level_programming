#!/usr/bin/python3
"""
script that lists all State objects containing the letter 'a'
"""
import sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine, select
if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    Session = session()
    stmt = select(State).where(State.name.like("%a%")).order_by(State.id)
    for state in Session.scalars(stmt):
        print(f"{state.id}: {state.name}")
    Session.close()
