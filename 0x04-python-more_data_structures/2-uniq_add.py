#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list.
    Args:
        my_list: The list of integers.
    Returns:
        The sum of the unique integers in the list.
    """
    return sum(set(my_list))
