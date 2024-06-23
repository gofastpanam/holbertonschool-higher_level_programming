#!/usr/bin/python3
"""
This module provides a class State links to the MYSQL table states
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
import sys


if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Enter 'username', 'pass', 'database_name'.")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    states = database.query(State).all()
    for state in states:
        print(state)

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, database), pool_pre_ping=True)
