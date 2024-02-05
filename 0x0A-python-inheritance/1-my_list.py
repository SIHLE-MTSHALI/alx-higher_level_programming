#!/usr/bin/python3
"""
Defines the MyList class that inherits from list, including a method to
print the list elements in ascending order.
"""


class MyList(list):
    """Inherits from list."""
    def print_sorted(self):
        """Prints the list in ascending order."""
        print(sorted(self))
