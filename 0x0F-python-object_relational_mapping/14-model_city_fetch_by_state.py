#!/usr/bin/python3
"""
This script prints all City objects from the database hbtn_0e_14_usa
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
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for city in session.query(City).join(State).order_by(City.id).all():
        print(f"{city.state.name}: ({city.id}) {city.name}")

    session.close()
