#!/usr/bin/python3
"""
This module provides a function that creates an Object from a “JSON file
”"""

import json


def load_from_json_file(filename):
    """
    This function creates an object from Json file
    Args:
        filename: the file to convert
    """
    with open(filename, "r", encoding="utf8") as file:
        json_str = file.read()
        object = json.loads(json_str)
        return object
