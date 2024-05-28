#!/usr/bin/python3
"""
This module provides a function that return an object
respresented by a JSON string:
"""

import json


def from_json_string(my_str):
    """
    This function return an object represented by a JSON string
    Args:
        my_str: JSON string
    Returns:
        Object in python
    """
    return json.loads(my_str)
