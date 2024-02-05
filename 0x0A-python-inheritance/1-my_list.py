#!/usr/bin/python3
"""
Module 1-my_list contains a class MyList that inherits from list and includes
a method to print the list in ascending order.
"""


class MyList(list):
    """
    MyList class inherits from list.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        print(sorted(self))
