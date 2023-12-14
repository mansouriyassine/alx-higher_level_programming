#!/usr/bin/python3
"""
This script prints the State object with a specific name from the database
hbtn_0e_6_usa. It uses SQLAlchemy for database interaction, ensuring
SQL injection safety by using parameterized queries.
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

    state_name = sys.argv[4]
    state = session.query(State).filter(State.name == state_name).first()

    if state:
        print(f"{state.id}")
    else:
        print("Not found")

    session.close()
