#!/usr/bin/python3
"""
This module provides a class BaseGeometry and subclass Rectangle
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
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        return (self.__width * self.__height)


class Square(Rectangle):
    """
    This is class Square
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))

    def area(self):
        return (self.__size * self.__size)
