#!/usr/bin/python3
"""The module of the square"""


class Square:
    """The quare's definition"""

    def __init__(self, size=0):
        """
        The new square's initialization
        Args:
            size: length of one side
        """
        self.size = size

    @property
    def size(self):
        """
        The square's side length
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
        The square's area
        Returns: The squared size
        """
        return self.__size ** 2

    def my_print(self):
        """Prints square with size of input"""
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="\n" if j is self.size - 1 and i != j else "")
        print()
