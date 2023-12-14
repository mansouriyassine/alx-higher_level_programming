#!/usr/bin/python3
"""
This script prints the first State object from the database hbtn_0e_6_usa.
It uses SQLAlchemy to connect to a MySQL database, queries the first state
based on the id order, and prints its details. If no states are found,
it prints 'Nothing'.
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

    first_state = session.query(State).order_by(State.id).first()
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    session.close()
