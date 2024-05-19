#!/usr/bin/python3

"""
This module defines a class Square which represents a square with a given size.
"""


class Square:
    """
    The Square class represents a square with a private size attribute.

    Attributes:
        size(int) : the size of a side of a square.
    """

    def __init__(self, size=0):
        """
        Initialise a new Square instance
        Args:
            size(int): The size of one size of the square. Default is 0.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.__size = size

    @property
    def size(self):
        """
        Get the current size of the square.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Set the size of the square.
        Args:
            value(int): The size of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Defines a method that returns the current square area.

        Return: multiplication of two sizes which give the square area
        """
        return (self.__size * self.__size)
