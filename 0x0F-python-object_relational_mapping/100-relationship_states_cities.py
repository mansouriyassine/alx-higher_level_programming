#!/usr/bin/python3
"""
Creates 'California' state with 'San Francisco' city in the database.
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine(
        f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}'
        f'@localhost/{sys.argv[3]}', pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)()

    california = State(name='California')
    san_francisco = City(name='San Francisco', state=california)

    session.add_all([california, san_francisco])
    session.commit()
    session.close()
