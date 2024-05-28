#!/usr/bin/python3
"""
This module provides a function that appends a string
at the end of a text file (UTF8)
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    This function appends a string at the end of a text file UTF8

    Args:
        filename: The file where writing the text
        text: the text to append in filename

    Return:
        The number os characters in the txt append
    """
    with open(filename, 'a', encoding='utf8') as file:
        file.write(text)
        for i in range(len(text)):
            i += 1

        return i
