#!/usr/bin/python3
"""
Module 11-square defines a Square class that inherits from Rectangle
and overrides the __str__ method to print square description.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle and has its own __str__ method.
    """

    def __init__(self, size):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the square sides.
        """
        super().__init__(size, size)  # Call to Rectangle's __init__
        self.__size = size  # Define private size

    def area(self):
        """
        Return the area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Return the square description for print() and str().
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
