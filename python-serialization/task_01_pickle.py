#!/usr/bin/python3
"""
This module serialize and deserialize custom Python objects
using the pickle module.
"""

import pickle


class CustomObject:
    """
    class named CustomObject
    """
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(self.name)
        print(self.age)
        print(self.is_student)
        
    def serialize(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)


    @classmethod
    def deserialize(cls, filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)
