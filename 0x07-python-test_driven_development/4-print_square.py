#!/usr/bin/python3
"""
Module: 4-print_square

Provides print_square(size) function to print a square of '#' characters.
"""


def print_square(size):
    """
    Prints a square of '#' with side length 'size'.

    Args:
        size (int): Length of one side of the square.

    Raises:
        TypeError: If 'size' is not an int.
        ValueError: If 'size' is a negative int.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if size > 0:
        print(("#" * size + "\n") * size, end="")
