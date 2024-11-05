#!/usr/bin/python3

""""""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

h = sys.argv[1]
p = sys.argv[2]
db = sys.argv[3]
search_name = sys.argv[4]

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(h, p, db))
    Session = sessionmaker(bind=engine)
    session = Session()

    newState = State(name="Louisiana")
    session.add(newState)
    session.commit()
    print(newState.id)