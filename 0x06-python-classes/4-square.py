#!/usr/bin/python3
"""The module of the square"""


class Square:
    """Defines square"""

    def __init__(self, size=0):
        """
        The new square is initialized
        Args:
            size: length of one side
        """
        self.size = size

    @property
    def size(self):
        """
        Finds the square's side length
        Raises:
            ValueError: if size is less than 0
            TypeError: if size is not int
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Finds the square's area
        Returns: The square's size
        """
        return self.__size ** 2
