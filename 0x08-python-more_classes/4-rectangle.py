#!/usr/bin/python3
"""Rectangle class implementation."""


class Rectangle:
    """Rectangle class for representing rectangles.

    Args:
        width (int, optional): The width of the rectangle. Defaults to 0.
        height (int, optional): The height of the rectangle. Defaults to 0.

    """
    def __init__(self, width=0, height=0):
        self.set_width(width)
        self.set_height(height)

    def set_width(self, width):
        """Set the width of the rectangle.

        Args:
            width (int): The width of the rectangle.

        Raises:
            ValueError: If width is less than 0.
            TypeError: If width is not an integer.

        """
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width

    def set_height(self, height):
        """Set the height of the rectangle.

        Args:
            height (int): The height of the rectangle.

        Raises:
            ValueError: If height is less than 0.
            TypeError: If height is not an integer.

        """
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.

        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.

        """
        return 2 * (self.__width + self.__height)

    def display(self):
        """Display the rectangle using '#' symbols."""
        for _ in range(self.__height):
            print('#' * self.__width)

    def __str__(self):
        """Return a string representation of the rectangle.

        Returns:
            str: A string representing the rectangle using '#' symbols.

        """
        return '\n'.join(['#' * self.__width] * self.__height)

    def __repr__(self):
        """Return a string representation of the rectangle object.

        Returns:
            str: A string representation that can be used to recreate
                 the object.

        """
        return f'Rectangle({self.__width}, {self.__height})'
