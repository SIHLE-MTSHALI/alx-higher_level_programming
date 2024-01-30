#!/usr/bin/python3
"""
This module provides a function to add two integers or floats.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats.

    Args:
        a: First number, must be an integer or float.
        b: Second number, must be an integer or float. Defaults to 98.

    Returns:
        The addition of a and b as an integer.

    Raises:
        TypeError: If either a or b is neither an integer nor a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
