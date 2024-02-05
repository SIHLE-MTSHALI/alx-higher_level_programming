#!/usr/bin/python3
"""
Module 10-square defines a Square class that inherits from Rectangle.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the square sides.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Return the area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Return the square description.
        """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
