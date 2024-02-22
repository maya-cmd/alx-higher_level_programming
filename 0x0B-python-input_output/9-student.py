#!/usr/bin/python3
"""Module for Student class"""


class Student:
    def __init__(self, first_name, last_name, age):
        """The constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Function retrieves a dictionary representation of a Student"""
        return self.__dict__
