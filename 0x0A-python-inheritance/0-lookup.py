#!/usr/bin/python3
"""Module for lookup"""


def lookup(obj):
    """Function returns object  attributes and methods
        Args:
            obj: The object
        Return:
            list:  Attributes list
    """
    return dir(obj)
