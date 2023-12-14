#!/usr/bin/python3
"""
This script lists all City objects from the database hbtn_0e_101_usa.
Each city's ID, name, and corresponding state name are displayed.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
import sys


if __name__ == "__main__":
    engine = create_engine(
        f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}'
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    for city in session.query(City).order_by(City.id).all():
        print(f"{city.id}: {city.name} -> {city.state.name}")

    session.close()
