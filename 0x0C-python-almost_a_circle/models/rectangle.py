#!/usr/bin/python3
"""Defines a rectangle class."""
import turtle
from models.base import Base


class Rectangle(Base):
    """Represent class  rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the new Rectangle class.

        Args:
            width (int): The width.
            height (int): The height .
            x (int): The x attribute.
            y (int): The y attribute.
            id (int): Identity of the new Rectangle
        Raises:
            TypeError: If either width or height is not an int.
            ValueError: If either  width or height <= 0.
            TypeError: If either  x or y is not an int.
            ValueError: If either x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Set and get the Rectangle width ."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Set and get the Rectangle height ."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Set and get the Rectangle's x attribute ."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Set and get the Rectangle's y attribute ."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
