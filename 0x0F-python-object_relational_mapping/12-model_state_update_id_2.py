#!/usr/bin/python3
"""
This script updates the name of the State object with id = 2 to 'New Mexico'
in the database hbtn_0e_6_usa using SQLAlchemy.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    engine = create_engine(
        f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}'
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    state_to_update = session.query(State).filter_by(id=2).first()

    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    session.close()
