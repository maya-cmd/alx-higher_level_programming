#!/usr/bin/python3
"""Module of Mylist class"""


class MyList(list):
    """Custom Mylist class"""
    def print_sorted(self):
        """
            print_sorted - prints list using ascending sort
        """
        print(sorted(self))
