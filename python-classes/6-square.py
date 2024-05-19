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
    
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialise a new Square instance
        
        Args:
            size(int): The size of one size of the square. Default is 0.
            position(int, int): The position for print the square
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.__size = size
        self.__position = position

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
        """
            
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Set the position for print the square 
        """
        return(self.__position)
         
    @position.setter
    def position(self, value):
         if not isinstance(value, tuple):
            print("position must be a tuple of 2 positive integers")
            raise(TypeError)
         else:
            self.__position = value


    def area(self):
        """
        Defines a method that returns the current square area.

        Return: multiplication of two sizes which give the square area
        """
        return (self.__size * self.__size)
    
    def my_print(self):
         """
         Prints a square with side of square egals size with # to stdout.
         """
         
         
         for h in range(0, self.__position[1]):
             print("")         
         for i in range(0, self.__size):
             print(" " * self.__position[0] + "#" * self.__size)
