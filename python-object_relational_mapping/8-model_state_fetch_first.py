#!/usr/bin/python3
"""
This module prints the first State object from the database hbtn_0e_6_usa
"""
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
            username, password, database), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).first()
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    session.close()
