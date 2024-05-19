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
        Initialise a new Square instance.
        Args:
            size(int): The size of one size of the square. Default is 0.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            pass
