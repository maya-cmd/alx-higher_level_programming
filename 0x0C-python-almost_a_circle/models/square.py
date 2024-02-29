#!/usr/bin/python3
"""Defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """The method initialize a new Square.

        Args:
            size (int): The newly created square size.
            x (int): The square's x coordinate.
            y (int): The square's y coordinate.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get and set the square's size."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
