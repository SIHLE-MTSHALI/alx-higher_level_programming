#!/usr/bin/python3
"""
Module to find a peak in an unsorted list of integers.
"""

def find_peak(list_of_integers):
    """
    Function to find a peak in an unsorted list of integers.
    A peak is an element greater than or equal to its neighbors.
    """
    if not list_of_integers:
        return None
    
    low = 0
    high = len(list_of_integers) - 1
    
    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid
    
    return list_of_integers[low]
