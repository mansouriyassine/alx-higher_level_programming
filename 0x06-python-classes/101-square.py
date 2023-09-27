#!/usr/bin/python3

class Square:
    def __init__(self, size=0, position=(0, 0)):
        self._size = self._validate_size(size)
        self._position = self._validate_position(position)

    def _validate_size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        return size

    def _validate_position(self, position):
        if (not isinstance(position, tuple) or
            len(position) != 2 or
            not all(isinstance(num, int) for num in position) or
            not all(num >= 0 for num in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        return position

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = self._validate_size(value)

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = self._validate_position(value)

    def area(self):
        return self._size * self._size

    def my_print(self):
        if self._size == 0:
            print()
            return

        for _ in range(self._position[1]):
            print()

        for _ in range(self._size):
            print(" " * self._position[0] + "#" * self._size)

    def __str__(self):
        if self._size == 0:
            return ""

        result = ""
        for _ in range(self._position[1]):
            result += "\n"

        for _ in range(self._size):
            result += " " * self._position[0] + "#" * self._size
            if _ < self._size - 1:
                result += "\n"

        return result
