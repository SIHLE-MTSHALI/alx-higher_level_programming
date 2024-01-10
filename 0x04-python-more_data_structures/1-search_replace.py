#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of an element by another in a new list.
    Args:
        my_list: The original list.
        search: The element to be replaced.
        replace: The new element that will replace the search element.
    Returns:
        A new list with elements replaced.
    """
    return [replace if x == search else x for x in my_list]
