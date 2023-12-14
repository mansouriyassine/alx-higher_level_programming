#!/usr/bin/python3
"""Rectangle Class Definition"""


class Rectangle:
    """A class representing a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize the Rectangle with the given width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return a human-readable string representation of the rectangle."""
        return f"Rectangle(width={self.width}, height={self.height})"

    def __repr__(self):
        """Return a string representation of the rectangle that can be used to recreate it."""
        return f"Rectangle({self.width}, {self.height})"
