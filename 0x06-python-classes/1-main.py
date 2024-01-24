#!/usr/bin/python3
"""
Test module for Square class with private size attribute
"""

Square = __import__('1-square').Square

my_square = Square(3)
print("Type of my_square is {}".format(type(my_square)))
print("Attributes of my_square: {}".format(my_square.__dict__))

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)
