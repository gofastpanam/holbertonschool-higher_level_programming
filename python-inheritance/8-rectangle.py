#!/usr/bin/python3
"""
This module provides a class
"""


class BaseGeometry():
    """
    This is a class which returns exception
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        if not isinstance(name, int):
            return


class Rectangle(BaseGeometry):
    """
    This is a class Rectangle
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

        if not isinstance(width, int) and not isinstance(height, int):
            raise TypeError
