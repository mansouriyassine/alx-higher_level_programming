#!/usr/bin/python3
"""Defines an extended list class MyList."""


class MyList(list):
    """An extension of the built-in list class with sorted printing."""

    def print_sorted(self):
        """Print the list in ascending order."""
        print(sorted(self))
