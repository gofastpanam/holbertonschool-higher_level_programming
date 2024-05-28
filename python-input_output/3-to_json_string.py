#!/usr/bin/python33
import json
"""
This module provides a function that returns
the JSON representation of an object (string)
"""


def to_json_string(my_obj):
    """
    This function return the json representation of an object
    Args:
        mt_obj: The object to convert in json
    Return:
        The json representation of object
    """
    json_str = json.dumps(my_obj)
    return json_str
