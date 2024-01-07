#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    Replaces an element in a list at a specific index without modifying
    the original list. Returns a copy of the list.
    """
    new_list = my_list.copy()
    if 0 <= idx < len(new_list):
        new_list[idx] = element
    return new_list
