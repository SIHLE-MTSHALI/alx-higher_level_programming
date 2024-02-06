#!/usr/bin/python3
"""
Defines a function that returns the dictionary description for JSON
serialization of an object.
"""


def class_to_json(obj):
    """Return the dictionary description for JSON serialization of an object.
    Args:
        obj (object): An instance of a Class.
    Returns:
        dict: Dictionary description of the object for JSON serialization.
    """
    return obj.__dict__
