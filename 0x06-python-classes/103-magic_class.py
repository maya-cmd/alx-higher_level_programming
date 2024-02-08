#!/usr/bin/python3

"""Defines a MagicClassthat matches a Holberton's bytecode."""

import math


class MagicClass:
    """Represents a circle."""

    def __init__(self, radius=0):
        """Initialization of a MagicClass.

        Arg:
            radius (float or int): The radius of the new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the MagicClass area."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return the  MagicClass circumference."""
        return (2 * math.pi * self.__radius)
