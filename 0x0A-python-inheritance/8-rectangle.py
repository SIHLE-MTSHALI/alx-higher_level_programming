#!/usr/bin/python3
"""
Module 8-rectangle defines a Rectangle class that inherits from BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A Rectangle that inherits from BaseGeometry.
    """
    def __init__(self, width, height):
        """
        Initializes the Rectangle with width and height after validation.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
