#!/usr/bin/python3
"""
Defines "Square" class inherited from "Rectangle."
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class: Inherit Rect
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Init Square with size.
        """
        super().__init__(id=id, x=x, y=y, width=size, height=size)

    def __str__(self):
        """String representation.
        """
        return '[Square] ({}) {}/{} - {}'.format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Size getter.
        """
        return self.width

    @size.setter
    def size(self, value):
        """Size setter, update width/height.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update attributes.
        """
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key in kwargs:
                if key == 'id':
                    self.id = kwargs['id']
                if key == 'size':
                    self.width = kwargs['size']
                if key == 'x':
                    self.x = kwargs['x']
                if key == 'y':
                    self.y = kwargs['y']

    def to_dictionary(self):
        """Dictionary representation.
        """
        square_dict = {}
        square_dict['id'] = self.id
        square_dict['size'] = self.width
        square_dict['x'] = self.x
        square_dict['y'] = self.y
        return square_dict
