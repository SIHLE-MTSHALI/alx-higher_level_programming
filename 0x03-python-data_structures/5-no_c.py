#!/usr/bin/env python3

def no_c(my_string):
    """
    Removes all characters 'c' and 'C' from a string.
    Returns the new string.
    """
    return ''.join(char for char in my_string if char not in ['c', 'C'])
