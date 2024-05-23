#!/usr/bin/python3
"""
This module provides a function which returns True if the object is exactly
of the specified class; otherwise False.
"""


def is_same_class(obj, a_class):
    """
    This function return True or False
    """
    if isinstance(obj, a_class):
        return True
    if not isinstance(obj, a_class):
        return False
