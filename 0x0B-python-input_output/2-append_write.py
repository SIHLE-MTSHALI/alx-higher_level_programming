#!/usr/bin/python3
"""
Module to append a string at the end of a text file (UTF-8) and return
the number of characters added.
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF-8) and returns number
    of characters added.
    Args:
        filename (str): The name of the file.
        text (str): The string to append to the file.
    Returns:
        int: The number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
