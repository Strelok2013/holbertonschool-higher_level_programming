#!/usr/bin/python3

"""
    Fetches All states and Cities
    which have a matching state_id.
    Prints them to output.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_state import City

h = sys.argv[1]
p = sys.argv[2]
db = sys.argv[3]
search_name = sys.argv[4]

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(h, p, db))
    Session = sessionmaker(bind=engine)
    session = Session()

    for state, city in session.query(State, City) \
            .filter(State.id == City.state_id) \
            .order_by(City.id):
        print("{}: ({}) {}".format(state.name, city))
