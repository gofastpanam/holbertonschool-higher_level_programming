#!/usr/bin/python3
"""
This module provides a function that reads a text file (UTF8) and prints it to stdou
"""

def read_file(filename=""):
    with open(filename, 'r', encoding='utf8') as file:
        print(file.read(), end="")
