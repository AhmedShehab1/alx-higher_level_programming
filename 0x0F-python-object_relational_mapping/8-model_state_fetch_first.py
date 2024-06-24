#!/usr/bin/python3
"""
script that prints the first State object from db
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
    Session = sessionmaker(bind=engine)
    session = Session()
    stmt = select(State).where(State.id == 1)
    try:
        state_1 = session.scalars(stmt).one()
        print(f"{state_1.id}: {state_1.name}")
    except Exception as e:
        print("Nothing")
    finally:
        session.close()
