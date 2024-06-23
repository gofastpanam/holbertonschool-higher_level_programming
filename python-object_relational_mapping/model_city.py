#!/usr/bin/python3
"""
Python file similar to model_state.py named model_city.py
that contains the class definition of a City"""
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base
import sys


class City(Base):
    """
    City class representing the cities table in the database.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)


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

    # Create all tables in the database
    Base.metadata.create_all(engine)
