#!/usr/bin/python3
"""
This module provides a class State links to the MYSQL table states
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    'mysql+mycient://{}:{}@localhost:3306/hbtn_0e_6_usa',
    echo=True)

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128))
