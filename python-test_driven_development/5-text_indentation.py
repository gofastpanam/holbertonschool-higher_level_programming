#!/usr/bin/python3
"""
This module profides a function that edit text with 2 new lines
after characters: (.) (?) (:)
"""


def text_indentation(text):
    """
    edit text with 2 new lines after special character and print new text
    Arg:
        text: the text to edit
    Raise:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_char = {".", "?", ":"}
    i = 0
    while i < len(text):
        print(text[i], end='')
        if text[i] in special_char:
            print("\n\n", end='')
            i += 1
            while i < len(text) and text[i] == ' ':
                i -= 1
        i += 1
