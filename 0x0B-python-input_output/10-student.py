#!/usr/bin/python3

class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None and all(isinstance(attr, str) for attr in attrs):
            return {
                attr: getattr(self, attr)
                for attr in attrs
                if hasattr(self, attr)
            }
        return self.__dict__
