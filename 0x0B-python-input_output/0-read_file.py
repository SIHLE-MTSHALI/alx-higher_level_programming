#!/usr/bin/python3
"""
Module 0-read_file contains a function that reads a text file (UTF-8)
and prints it to stdout.
"""


def read_file(filename=""):
    """Read a text file (UTF-8) and print it to stdout."""
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')
