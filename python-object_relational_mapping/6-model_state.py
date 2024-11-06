#!/usr/bin/python3
"""
    Not part of the assignment,
    Here for testing purposes
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

h = sys.argv[1]
p = sys.argv[2]
db = sys.argv[3]

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
