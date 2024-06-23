#!/usr/bin/python3
"""
This module prints the State object with
the name passed as argument from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":

    if len(sys.argv) != 5:
        print("Enter 'user', 'pass', 'db name', 'state name'.")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name_to_search = sys.argv[4]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, database,))

    Session = sessionmaker(bind=engine)
    session = Session()

    states_searched = session.query(State).filter_by(
        name='state_name_to_search'.all())
    if states_searched is None:
        print("Not found")
    else:
        for state in states_searched:
            print(state.id)

    session.close()
