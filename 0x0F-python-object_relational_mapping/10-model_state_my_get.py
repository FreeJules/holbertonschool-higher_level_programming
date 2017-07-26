#!/usr/bin/python3
'''
prints the State object with the name passed as argument
'''
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    search_for = sys.argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    '''
    for state in session.query(State).filter(State.name == search_for):
        if state:
            print("{}".format(state.id))
    '''
    try:
        state = session.query(State).filter(State.name == search_for).one()
        print("{}".format(state.id))
    except:
        print("Not found")
    session.close()
