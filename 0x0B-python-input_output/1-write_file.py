#!/usr/bin/python3
"""Module for write_file method"""


def write_file(filename="", text=""):
    """
    Function writes a string to a text file (UTF8)

    Returns:
        the number of characters written.
    """

    with open(filename, 'w', encoding='utf-8') as file:
        file_content = file.write(text)
        return file_content
