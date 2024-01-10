#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds a key/value in a dictionary.
    Args:
        a_dictionary: The original dictionary.
        key: The key to update or add.
        value: The value associated with the key.
    Returns:
        The updated dictionary.
    """
    a_dictionary[key] = value
    return a_dictionary
