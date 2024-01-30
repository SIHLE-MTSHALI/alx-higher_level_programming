#!/usr/bin/python3
"""
This module provides a function to print text with special indentation.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'.

    Args:
        text: The text to be printed. Must be a string.

    Raises:
        TypeError: If the text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            if i < len(text) - 1 and text[i + 1] == " ":
                i += 1
        i += 1
