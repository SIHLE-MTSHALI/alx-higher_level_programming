#!/usr/bin/python3
"""
Module 100-my_int defines a class MyInt that inherits from int and inverts
the == and != operators.
"""


class MyInt(int):
    """
    MyInt is a subclass of int with inverted == and != operators.
    """

    def __eq__(self, other):
        """
        Invert the == operator.
        """
        return super().__eq__(other) is False

    def __ne__(self, other):
        """
        Invert the != operator.
        """
        return super().__eq__(other) is True
