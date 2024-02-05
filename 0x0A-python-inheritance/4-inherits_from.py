#!/usr/bin/python3
"""
Module 4-inherits_from contains a single function inherits_from which
checks for object inheritance from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Return True if obj is an instance of a class that inherited (directly or
    indirectly) from the specified class; otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
