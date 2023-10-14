#!/usr/bin/python3
import json


class Base:
    """Base class for managing instances in JSON files."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base instance with an id."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dictionaries."""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return a list of dictionaries represented by a JSON string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of objects to a JSON file."""
        filename = cls.__name__ + ".json"
        objects = []
        if list_objs:
            objects = [obj.to_dictionary() for obj in list_objs]
        with open(filename, mode='w', encoding='utf-8') as file:
            file.write(cls.to_json_string(objects))

    @classmethod
    def load_from_file(cls):
        """Load objects from a JSON file and return a list of instances."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                data = cls.from_json_string(file.read())
                return [cls.create(**obj) for obj in data]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the Turtle graphics module."""
        import turtle

        screen = turtle.Screen()
        screen.title("Shapes Drawing")

        t = turtle.Turtle()

        def draw_rectangle(x, y, width, height):
            t.penup()
            t.goto(x, y)
            t.pendown()
            t.forward(width)
            t.left(90)
            t.forward(height)
            t.left(90)
            t.forward(width)
            t.left(90)
            t.forward(height)
            t.left(90)

        for rectangle in list_rectangles:
            t.color("blue")
            draw_rectangle(rectangle.x, rectangle.y,
            rectangle.width, rectangle.height)

        for square in list_squares:
            t.color("red")
            draw_rectangle(square.x, square.y, square.size, square.size)

        turtle.done()
