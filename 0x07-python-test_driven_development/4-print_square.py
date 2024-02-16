#!/usr/bin/python3

"""
Module print_square

prints a square with the character #
"""


def print_square(size):
    """
    The function prints a square with the character #
    Args:
        size: The size of square
    Returns:
        A square that is printed
    Raises:
        TypeError and Value Error
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print((("#" * size + '\n') * size), end="")

    if __name__ == "__main___":
        import doctest
        doctest.testfile("tests/4-print_square.txt")
