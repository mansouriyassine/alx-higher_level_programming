#!/usr/bin/python3
"""
This script prints all City objects from the hbtn_0e_14_usa database.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys

if __name__ == "__main__":
    engine = create_engine(
        f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}'
        f'@localhost/{sys.argv[3]}'
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    for city, state in session.query(City, State).join(State) \
            .order_by(City.id).all():
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
