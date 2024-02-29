#!/usr/bin/python3

"""Define a base model class"""
import turtle
import json
import csv


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Method outputsthe JSON serialization of a dicts'list.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
