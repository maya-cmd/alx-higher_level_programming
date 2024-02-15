#!/usr/bin/python3

"""
Module that returns the addition of two integers.

"""


def add_integer(a, b=98):
    """
    Function that adds two integers together.
    Args:
        a: first int
        b: second int, which is 98 by default 
    Returns: sum of a and b
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
