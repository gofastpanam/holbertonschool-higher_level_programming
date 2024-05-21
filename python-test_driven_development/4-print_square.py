#!/usr/bin/python3
"""
This module provides a square with the character #
"""


def print_square(size):
    """
    Print a square with character # with lenght of side is size
    Args:
        size: The size of side of the square
    Raises:
        TypeError: If size is not integer
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        print("#" * size)
