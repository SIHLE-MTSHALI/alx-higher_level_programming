#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    Replaces an element in a list at a specific index.
    Does nothing if the index is negative or out of range.
    Returns the original or modified list.
    """
    if 0 <= idx < len(my_list):
        my_list[idx] = element
    return my_list
