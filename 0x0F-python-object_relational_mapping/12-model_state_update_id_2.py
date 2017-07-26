#!/usr/bin/python3
'''
changes the name of a State object from the database hbtn_0e_6_usa
'''
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    new_state = State(name='Louisiana')
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    update_state = session.query(State).filter(State.id == 2).one()
    update_state.name = "New Mexico"
    session.commit()
    session.close()
