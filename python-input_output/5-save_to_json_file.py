#!/usr/bin/python3
"""
This module provides a function that writes an Object
to a text file, using a JSON representation
"""

import json


def save_to_json_file(my_obj, filename):
    """
    This function writes an Object to a text file, using a JSON representation
    Args:
        my_obj: The object to convert in json and print in file
        filename: the file where to print result
    Returns
        The result in json
    """
    with open(filename, 'w') as file:
        file.write(json.dumps(my_obj))
