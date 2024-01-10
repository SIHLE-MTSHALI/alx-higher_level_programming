#!/usr/bin/python3

def best_score(a_dictionary):
    """
    Returns the key with the biggest integer value.
    Args:
        a_dictionary: The dictionary to search through.
    Returns:
        The key with the highest value, or None if the dictionary is empty.
    """
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
