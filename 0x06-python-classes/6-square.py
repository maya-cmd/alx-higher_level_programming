#!/usr/bin/python3
"""The  Module of the square"""


class Square:
    """the square's defnition"""

    def __init__(self, size=0, position=(0, 0)):
        """
        The square class is initialized
        Args:
            size(int): length of one side
            position(int, int): position of square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        The current size of square is set
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

    @property
    def position(self):
        """
        The current position of square is set
        """
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Fnds the square's area
        Returns: The square's size
        """
        return self.__size ** 2

    def my_print(self):
        """The square is printed using # character"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print()
