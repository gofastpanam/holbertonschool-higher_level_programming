#!/usr/bin/python3
"""
This module lists all State objects that contain the letter a
from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Enter 'username', 'pass', 'database_name'.")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, database))

    Session = sessionmaker(bind=engine)
    session = Session()

    states_a = session.query(State).filter(
        State.name.ilike('%a%')).order_by(State.id).all()
    for state in states_a:
        print("{0}: {1}".format(states_a.id, states_a.name))

    session.close()
