#!/usr/bin/python3
"""
This module serves as the foundation for all other classes in this project.
"""

import json
import os


class Base:
    """Base Class used as a blueprint for other classes.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor for setting the 'id' attribute.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries=[]):
        """Serialize a list into JSON format.
        """
        if not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list to a file after serializing it to JSON.
        """
        list_data = [] if list_objs is None else \

        filename = cls.__name__ + '.json'
        with open(filename, mode='w+') as file:
            file.write(cls.to_json_string(list_data))

    @staticmethod
    def from_json_string(json_string):
        """Parse a JSON string and return a list.
        """
        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance of the class using a dictionary.
        """
        instance = cls(8, 8, 8, 8)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """Load data from a JSON file and create instances.
        """
        filename = cls.__name__ + '.json'
        with open(filename, mode='r') as file:
            file_contents = file.read()
        if file_contents:
            data_list = cls.from_json_string(file_contents)
            instance_list = []
            for data in data_list:
                instance_list.append(cls.create(**data))
            return instance_list
        else:
            return []
