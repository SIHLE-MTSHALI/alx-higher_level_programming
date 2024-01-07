#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """
    Finds all multiples of 2 in a list.
    Returns a new list with True or False for each element,
    indicating whether it is divisible by 2.
    """
    return [num % 2 == 0 for num in my_list]
