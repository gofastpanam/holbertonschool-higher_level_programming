#!/usr/bin/python3
import sys
"""
This module provides a script that adds all arguments
to a Python list, and then save them to a file
"""

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"

try:
    list = load_from_json_file(filename)
except FileNotFoundError:
    list = []

list += sys.argv[1:]
save_to_json_file(list, filename)
