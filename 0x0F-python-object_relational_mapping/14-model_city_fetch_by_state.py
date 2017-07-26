#!/usr/bin/python3
'''
prints all City objects from the database hbtn_0e_14_usa
'''
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for state, city in session.query(State, City).filter(State.id ==
                                                         City.state_id).all():
        print('{}: '.format(state.name), end='')
        print('({}) {}'.format(city.id, city.name))
    session.close()
