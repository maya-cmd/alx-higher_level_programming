#!/usr/bin/python3
"""Rectangle Module"""


class Rectangle:
    """Defines rectangle"""

    number_of_instances = 0

    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Args:
            width: The rectangle's width
            height: The rectangle's height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Obtains the width of the rectangle
            Returns:
                ValueError: if width is less than 0
                TypeError: if width not integer
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Obtains the height of rectangle
        Returns:
                ValueError: if height is less than 0
                TypeError: if height not integer
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        returns the rectangle area
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        returns the rectangle's perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """print the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += str(self.print_symbol) * self.__width + "\n"
        return rectangle_str[:-1]

    def __repr__(self):
        """return a the rectangle's string representation"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print the message Bye rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two rectangles
        Args:
            rect_1: First rectangle
            rect_2: Second reactangle
        Returns: bigger rectangle or rect_1 if both equal
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1
