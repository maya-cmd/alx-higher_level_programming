#!/usr/bin/python3
"""A square's  Module"""


class Square:
    """Class square is defined"""

    def __init__(self, size=0):
        """
        The new square is initialized
        Args:
            size: length of one side
        Raises:
            ValueError: if size is less than 0
            TypeError: if size is not int
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Finds the area of a square
        Returns: The squared size
        """
        return self.__size ** 2
