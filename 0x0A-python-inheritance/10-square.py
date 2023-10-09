#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle (9-rectangle.py)."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square using Rectangle."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the new Square.
        """
        super().__init__(size, size)

    def __str__(self):
        """Return a string representation of the Square."""
        return "[Square] {}/{}".format(self.__width, self.__height)
