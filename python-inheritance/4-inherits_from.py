#!/usr/bin/python3
"""
This module provides a function that returns True if the object is
an instance of a class that inherited from specified class;
otherwise False
"""


def inherits_from(obj, a_class):
    """
    Returns True or False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
