#!/usr/bin/python3

"""Define a base model class"""
import turtle


class Base:
    """Defines a base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Method responsible for assigning the public instance attribute id
        Args:
           id(int): integer value that manages id
        Return:
           Always none
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
