#!/usr/bin/python3

"""
    Fetches all entries in the states table
    Then prints all states that have the letter
    'a' in them.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

h = sys.argv[1]
p = sys.argv[2]
db = sys.argv[3]

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(h, p, db))
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id)
    for state in states:
        if "a" in state.name:
            print("{}: {}".format(state.id, state.name))
