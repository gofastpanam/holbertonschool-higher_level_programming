#!/usr/bin/python3
"""
This module provides a lists all City objects from the database 
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City  
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

    cities = session.query(City).order_by(city.id).all()
    for city in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()