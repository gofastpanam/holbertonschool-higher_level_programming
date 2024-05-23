#!/usr/bin/python3
"""
This module provides a function which returns list of
available attributes
"""


def lookup(obj):
    """
    This function prints the list of available attributes
    """
    print(dir(obj))
