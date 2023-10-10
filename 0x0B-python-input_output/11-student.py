#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, selected_attrs=None):
        """Get a dictionary representation of the Student.

        If selected_attrs is a list of strings, it represents only those
        attributes included in the list.

        Args:
            selected_attrs (list): (Optional) The attributes to include in
            the representation.
        """
        if (selected_attrs and isinstance(selected_attrs, list) and
                all(isinstance(attr, str) for attr in selected_attrs)):
            return {key: getattr(self, key) for key in selected_attrs if
                    hasattr(self, key)}
        return self.__dict__

    def reload_from_json(self, json_data):
        """Replace all attributes of the Student.

        Args:
            json_data (dict): The key/value pairs to replace attributes with.
        """
        for key, value in json_data.items():
            setattr(self, key, value)
