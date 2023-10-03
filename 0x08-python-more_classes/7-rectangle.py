#!/usr/bin/python3
"""Rectangle class implementation for Holberton Python project 0x08 task 7."""


class Rectangle:
    """A class to represent rectangles.

    Attributes:
        number_of_instances (int): A counter for the number of instances
        print_symbol (str): The symbol used for printing rectangles.

    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.

        Raises:
            ValueError: If either width or height is less than 0.
            TypeError: If either width or height is not an integer.

        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Get or set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Get or set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

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

    def __str__(self):
        """Return a string representation of the rectangle.

        Returns:
            str: A string representing the rectangle using '#' symbols.

        """
        if self.__width == 0 or self.__height == 0:
            return ''
        rectangle = []
        for _ in range(self.__height):
            rectangle.append(str(self.print_symbol) * self.__width)
        return '\n'.join(rectangle)

    def __repr__(self):
        """Return a string representation of the rectangle object.

        Returns:
            str: A string representation that can be used to recreate
                 the object.

        """
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        """Destructor for Rectangle instances.

        Prints a message when an instance is deleted.

        """
        type(self).number_of_instances -= 1
        print('Bye rectangle...')
