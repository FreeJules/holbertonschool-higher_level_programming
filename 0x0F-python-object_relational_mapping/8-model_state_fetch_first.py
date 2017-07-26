#!/usr/bin/python3
#!/usr/bin/python3
'''
prints the first State object from the database hbtn_0e_6_usa
'''
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).order_by(State.id)[0:1]:
        if state:
            print("{}: {}".format(state.id, state.name))
        else:
            print("Nothing")
    session.close()
