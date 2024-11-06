#!/usr/bin/python3

"""
    Modifies the entry with ID=2
    in the states table.
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

    target_entry = session.query(State).filter_by(id=2).first()

    target_entry.name = "New Mexico"

    session.commit()
