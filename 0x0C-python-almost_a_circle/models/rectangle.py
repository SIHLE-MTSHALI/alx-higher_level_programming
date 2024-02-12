#!/usr/bin/python3
"""
Defines the Rectangle class that inherits from Base.
"""
from .base import Base  # Corrected import statement


class Rectangle(Base):
    """Represents a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the Rectangle instance."""
        return self.width * self.height

    def display(self):
        """Print the Rectangle instance using the '#' character."""
        for row in range(self.height):
            print("#" * self.width)

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width, self.height))

    def display(self):
        """Print the Rectangle instance with '#' taking care of x and y."""
        print("\n" * self.y, end="")
        for row in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args):
        """Update the Rectangle attributes."""
        attrs = ['id', 'width', 'height', 'x', 'y']
        for attr, value in zip(attrs, args):
            setattr(self, attr, value)

    def update(self, *args, **kwargs):
        """Update the Rectangle attributes."""
        attrs = ['id', 'width', 'height', 'x', 'y']
        if args and len(args) > 0:
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)
