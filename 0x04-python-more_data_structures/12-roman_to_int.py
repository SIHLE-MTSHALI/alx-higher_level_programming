#!/usr/bin/python3

def roman_to_int(roman_string):
    """
    Convert a Roman numeral to an integer. If input is not a string or is
    None, return 0.
    """
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                  'M': 1000}
    int_val, prev_value = 0, 0
    for char in reversed(roman_string):
        value = roman_dict[char]
        int_val = int_val - value if value < prev_value else int_val + value
        prev_value = value
    return int_val
