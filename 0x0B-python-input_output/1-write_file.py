#!/usr/bin/python3
"""
This module defines a function that writes a string to a text file (UTF-8) and
returns the number of characters written.
"""


def write_file(filename="", text=""):
    """Write a string to a text file (UTF-8) and return number of characters.
    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write to the file.
    Returns:
        int: The number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
