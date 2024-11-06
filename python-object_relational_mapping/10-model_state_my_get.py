#!/usr/bin/python3

"""
    Fetches all entries in the state table
    Then prints the entry with the matching name
    passed in as the 4th argument.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

h = sys.argv[1]
p = sys.argv[2]
db = sys.argv[3]
search_name = sys.argv[4]

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(h, p, db))
    Session = sessionmaker(bind=engine)
    session = Session()

    found = False
    states = session.query(State).order_by(State.id)
    for state in states:
        if state.name == search_name:
            print("{}".format(state.id))
            found = True
            break
        if found is False:
            print("Not found")
