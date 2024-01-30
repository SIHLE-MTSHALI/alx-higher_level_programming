#!/usr/bin/python3
class LockedClass:
    """
    This class allows creating objects with a limited set of attributes.
    Specifically, only an attribute 'first_name' is allowed.
    """
    __slots__ = ['first_name']
