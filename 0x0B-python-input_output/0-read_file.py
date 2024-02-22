#!/usr/bin/python3
"""Module for read_file method"""


def read_file(filename=" "):
    """
    The method reads a text file and prints its content to stdout.

    Args:
        filename (str): The text file name.
    """

    with open(filename, 'r', encoding='utf-8') as file:
        file_content = file.read()
        print(file_content, end="")
