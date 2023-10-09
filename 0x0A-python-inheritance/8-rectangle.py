#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """Return a string representation of the Rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """Compute the area of the Rectangle.

        Returns:
            int: The area of the Rectangle.
        """
        return self.__width * self.__height
