#!/usr/bin/python3

"""A square's Module"""


class Square:

    """A square class's definition"""
    def __init__(self, size=0):

        """A new instance of the Square class is initialized."""

        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
