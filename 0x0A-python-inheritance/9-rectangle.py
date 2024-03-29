#!/usr/bin/python3
"""
Module 9-rectangle extends BaseGeometry with a Rectangle class, including
area calculation and a custom string representation.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A Rectangle that inherits from BaseGeometry, with additional features.
    """

    def __init__(self, width, height):
        """
        Initialize the Rectangle with width and height after validation.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Return the area of the Rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return the string representation of the Rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
