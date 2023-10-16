#!/usr/bin/python3
"""
This module defines the Rectangle class which inherits from the Base class.
"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class for geometric operations.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance with the specified dimensions.
        """
        if not isinstance(width, int):
            raise TypeError("Width must be an integer")
        if not isinstance(height, int):
            raise TypeError("Height must be an integer")
        if not isinstance(x, int):
            raise TypeError("X must be an integer")
        if not isinstance(y, int):
            raise TypeError("Y must be an integer")
        if width <= 0:
            raise ValueError("Width must be > 0")
        if height <= 0:
            raise ValueError("Height must be > 0")
        if x < 0:
            raise ValueError("X must be >= 0")
        if y < 0:
            raise ValueError("Y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter method for width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width attribute."""
        if not isinstance(value, int):
            raise TypeError('Width must be an integer')
        if value <= 0:
            raise ValueError('Width must be > 0')
        self.__width = value

    @property
    def height(self):
        """Getter method for height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height attribute."""
        if not isinstance(value, int):
            raise TypeError('Height must be an integer')
        if value <= 0:
            raise ValueError('Height must be > 0')
        self.__height = value

    @property
    def x(self):
        """Getter method for x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for x attribute."""
        if not isinstance(value, int):
            raise TypeError('X must be an integer')
        if value < 0:
            raise ValueError('X must be >= 0')
        self.__x = value

    @property
    def y(self):
        """Getter method for y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for y attribute."""
        if not isinstance(value, int):
            raise TypeError('Y must be an integer')
        if value < 0:
            raise ValueError('Y must be >= 0')
        self.__y = value

    def area(self):
        """Calculates the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """Displays the rectangle with '#' characters."""
        string1 = ('\n' * self.__y)
        string2 = ((" " * self.__x) + '#' * self.__width + '\n') * (
                (self.__height) - 1)
        string3 = ((" " * self.__x) + '#' * self.__width)
        print(string1 + string2 + string3)

    def __str__(self):
        """Returns a string representation of the object."""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - " \
               f"{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """Updates the attributes of the rectangle."""
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value

    def to_dictionary(self):
        """Returns a dictionary representation of the object."""
        return {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y
        }
