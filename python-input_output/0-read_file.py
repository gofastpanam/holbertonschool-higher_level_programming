#!/usr/bin/python3
"""
This module provides a function that reads
a text file (UTF8) and prints it to stdou
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.
    Args:
        filename (str): The name of the file to read.
        Defaults to an empty string.
    """
    with open(filename, 'r', encoding='utf8') as file:
        print(file.read(), end="")
