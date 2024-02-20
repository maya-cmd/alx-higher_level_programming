#!/usr/bin/python3
"""Modue for inherits_from method"""


def inherits_from(obj, a_class):
    """
    Function determines the saidobject is a true subclass of a class
    """
    return isinstance(obj, a_class) and type(obj) != a_class
