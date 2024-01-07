#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """
    Adds two tuples, each potentially containing two integers.
    If a tuple has less than 2 integers, it assumes 0 for the missing values.
    If a tuple has more than 2 integers, it only uses the first two.
    """
    a1, a2 = (tuple_a + (0, 0))[:2]
    b1, b2 = (tuple_b + (0, 0))[:2]
    return (a1 + b1, a2 + b2)
