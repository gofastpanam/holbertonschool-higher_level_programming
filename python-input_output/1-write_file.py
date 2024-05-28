#!/usr/bin/python3
"""
This module provides a function that writes a string to a text file (UTF8)
and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Reads a text file (utf8) and return the number of characters

    Args:
        filename: (str): The name of the file to write.
        If file is empty, create a new one.
        text: the text to print in file and to count the number of characters

    Return:
        Number of characters.
    """
    with open(filename, 'w', encoding='utf8') as file:
        file.write(text)
        for i in range(len(text)):
            i += 1
    return i
