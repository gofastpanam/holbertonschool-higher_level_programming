#!/usr/bin/python3
"""
This module provides a basic serialisation to serialize
a Python dictionary to a JSON file and deserialize
the JSON file to recreate the Python dictionary.
"""

import json


def serialize_and_save_to_file(data, filename):
    with open(filename, 'w') as file:
        file.write(json.dumps(data))
    pass


def load_and_deserialize(filename):
    with open(filename, 'r') as file:
        file.read(json.loads(data))
    pass
