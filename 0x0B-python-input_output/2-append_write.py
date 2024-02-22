#!/usr/bin/python3
"""Module for append_write method"""


def append_write(filename="", text=""):
    """
    The function appends a string at the end of a text file (UTF8)

    Returns:
        the number of characters added.
    """

    with open(filename, 'a', encoding='utf-8') as file:
        file_content = file.write(text)
        return file_content
