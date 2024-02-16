#!/usr/bin/python3
"""Module for say_may_name method"""


def say_my_name(first_name, last_name=""):
    """
    Function prints My name is <first name> <last name>
    Args:
        first_name: The first name
        Second_name: The . second name
    Returns:
        First name and second name
    Raises:
        TypeError if first and last name are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
