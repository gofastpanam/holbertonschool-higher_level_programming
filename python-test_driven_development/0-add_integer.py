#!/usr/bin/python3
"""
This module provides a function `add_integer` that adds two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats, casting them to integers if necessary.
    Args:
        a: The first number (int or float).
        b: The second number (int or float), defaults to 98.
    Returns:
        The sum of the two numbers, casted to an integer.
    Raises:
        TypeError: If either `a` or `b` is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
