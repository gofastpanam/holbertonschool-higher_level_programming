#!/usr/bin/python3
"""
This module provides a function that returns
the JSON representation of an object (string)
"""

import json


def to_json_string(my_obj):
    """
    This function return the json representation of an object
    Args:
        my_obj: The object to convert in json
    Returns:
        The json representation of object
    """
    return json.dumps(my_obj)
