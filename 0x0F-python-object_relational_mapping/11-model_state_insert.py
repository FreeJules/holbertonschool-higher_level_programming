#!/usr/bin/python3
'''
adds the State object "Louisiana" to the database hbtn_0e_6_usa
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
    session.add(new_state)
    session.commit()
    print("{}".format(new_state.id))
    session.close()
