#!/usr/bin/python3

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class, inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for the Square class."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size attribute."""
        return self.__width

    @size.setter
    def size(self, value):
        """Setter for size attribute."""
        self.width = value
        self.height = value

    def __str__(self):
        """Override the __str__ method to return a custom string format."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
            )

    def update(self, *args, **kwargs):
        """Update attributes with arguments or keyword arguments."""
        attributes = ["id", "size", "x", "y"]
        if args:
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation of the Square."""
        return {
            'id': self.id,
            'size': self.__width,
            'x': self.x,
            'y': self.y
        }
