#!/usr/bin/python3
"""
This module provides a class that inherits from list
"""


class MyList(list):
    """
    This class inherits from list
    """

    def print_sorted(self):
        list_sorted = sorted(self)
        print(list_sorted)
