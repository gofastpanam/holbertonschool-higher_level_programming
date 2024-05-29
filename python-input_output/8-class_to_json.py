#!/usr/bin/python3
"""
This module provides  a function that returns the dictionary description
with simple data structure for JSON serialization of an object.
"""

import json
import sys


def class_to_json(obj):
    """
    This function returns the dictionary description with simple data structure
    for JSON serializatoin of an object.
    Args:
        obj: instance of a class
    Returns:
        dictionary description
    """
    return (obj.__dict__)
