#!/usr/bin/python3
"""
Module 0-lookup contains the lookup function that returns a list of
available attributes and methods of an object.
"""


def lookup(obj):
    """Return the list of attributes and methods of an object."""
    return dir(obj)
