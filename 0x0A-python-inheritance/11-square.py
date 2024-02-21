#!/usr/bin/python3
"""Module for Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A subclass  of rectangle representing a square"""
    def __init__(self, size):
        """constructor"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Method for computing the square's area"""
        return self.__size ** 2

    def __str__(self):
        """returns string representation of square"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
