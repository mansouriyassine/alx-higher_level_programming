#!/usr/bin/python3
"""Unittests for models/base.py"""

import unittest
import os
import sys
import io
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""

    def test_no_id(self):
        b = Base()
        self.assertEqual(b.id, 1)

    def test_id_set(self):
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_id_negative(self):
        b = Base(-3)
        self.assertEqual(b.id, -3)

    def test_id_float(self):
        b = Base(4.5)
        self.assertEqual(b.id, 4.5)

    def test_id_string(self):
        b = Base("string")
        self.assertEqual(b.id, "string")

class TestBase_to_json_string(unittest.TestCase):
    """Unittests for testing to_json_string method of the Base class."""

    def test_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_none_list(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        dic = Base.to_json_string([r1.to_dictionary(), r2.to_dictionary()])
        self.assertTrue(type(dic) is str)

    def test_to_json_string_output(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        dic = Base.to_json_string([r1.to_dictionary(), r2.to_dictionary()])
        self.assertEqual(
            dic, '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}, {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]'
        )

class TestBase_save_to_file(unittest.TestCase):
    """Unittests for testing save_to_file method of the Base class."""

    def test_save_empty_list(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) > 0)

class TestBase_from_json_string(unittest.TestCase):
    """Unittests for testing from_json_string method of the Base class."""

    def test_from_json_string_empty(self):
        self.assertEqual(Rectangle.from_json_string("[]"), [])

    def test_from_json_string_none(self):
        self.assertEqual(Rectangle.from_json_string(None), [])

    def test_from_json_string(self):
        json_string = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}, {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]'
        list_objs = Rectangle.from_json_string(json_string)
        self.assertTrue(type(list_objs) is list)

    def test_from_json_string_output(self):
        json_string = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}, {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]'
        list_objs = Rectangle.from_json_string(json_string)
        self.assertEqual(len(list_objs), 2)
        self.assertTrue(type(list_objs[0]) is Rectangle)

class TestBase_create(unittest.TestCase):
    """Unittests for testing create method of the Base class."""

    def test_create_instance(self):
        r = Rectangle(3, 5)
        r_dictionary = r.to_dictionary()
        r1 = Rectangle.create(**r_dictionary)
        self.assertNotEqual(r, r1)
        self.assertFalse(r is r1)
        self.assertEqual(r, r1)

    def test_create_instance_square(self):
        s = Square(5)
        s_dictionary = s.to_dictionary()
        s1 = Square.create(**s_dictionary)
        self.assertNotEqual(s, s1)
        self.assertFalse(s is s1)
        self.assertEqual(s, s1)

class TestBase_load_from_file(unittest.TestCase):
    """Unittests for testing load_from_file method of the Base class."""

    def test_load_empty_list(self):
        Rectangle.save_to_file([])
        list_objs = Rectangle.load_from_file()
        self.assertEqual(list_objs, [])

    def test_load_no_file(self):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        list_objs = Rectangle.load_from_file()
        self.assertEqual(list_objs, [])

    def test_load_rectangle_list(self):
        r = Rectangle(2, 2)
        r1 = Rectangle(1, 1)
        Rectangle.save_to_file([r, r1])
        list_objs = Rectangle.load_from_file()
        self.assertTrue(type(list_objs) is list)
        self.assertEqual(len(list_objs), 2)
        self.assertTrue(type(list_objs[0]) is Rectangle)
        self.assertTrue(type(list_objs[1]) is Rectangle)

    def test_load_square_list(self):
        s = Square(2)
        s1 = Square(1)
        Square.save_to_file([s, s1])
        list_objs = Square.load_from_file()
        self.assertTrue(type(list_objs) is list)
        self.assertEqual(len(list_objs), 2)
        self.assertTrue(type(list_objs[0]) is Square)
        self.assertTrue(type(list_objs[1]) is Square)

class TestBase_max_integer(unittest.TestCase):
    """Unittests for testing max_integer method of the Base class."""

    def test_empty(self):
        self.assertEqual(Base.max_integer([]), 0)

    def test_max_integers(self):
        lst = [10, 0, -10, 5]
        self.assertEqual(Base.max_integer(lst), 10)

    def test_max_integers_unordered(self):
        lst = [5, 10, -10, 0]
        self.assertEqual(Base.max_integer(lst), 10)

    def test_max_integers_negative(self):
        lst = [-2, -5, -1]
        self.assertEqual(Base.max_integer(lst), -1)

    def test_max_integers_floats(self):
        lst = [5.5, 6.3, 5.2]
        self.assertEqual(Base.max_integer(lst), 6.3)

    def test_max_integers_string(self):
        lst = [5, 2, "string"]
        with self.assertRaises(TypeError):
            Base.max_integer(lst)

class TestBase_read_file(unittest.TestCase):
    """Unittests for testing read_file method of the Base class."""

    def test_read_empty_file(self):
        with open("empty.txt", "w") as f:
            pass
        self.assertEqual(Base.read_file("empty.txt"), "")

    def test_read_file(self):
        with open("text.txt", "w") as f:
            f.write("Hello, World!")
        self.assertEqual(Base.read_file("text.txt"), "Hello, World!")

class TestBase_write_file(unittest.TestCase):
    """Unittests for testing write_file method of the Base class."""

    def test_write_file(self):
        Base.write_file(["Hello, World!"], "text.txt")
        with open("text.txt", "r") as f:
            self.assertEqual(f.read(), "Hello, World!")

class TestBase_save_load_rectangles(unittest.TestCase):
    """Unittests for testing saving and loading of Rectangle objects."""

    def test_save_load_empty_rectangles(self):
        Rectangle.save_to_file([])
        list_objs = Rectangle.load_from_file()
        self.assertEqual(list_objs, [])

    def test_save_load_rectangles(self):
        r = Rectangle(2, 2)
        r1 = Rectangle(1, 1)
        Rectangle.save_to_file([r, r1])
        list_objs = Rectangle.load_from_file()
        self.assertTrue(type(list_objs) is list)
        self.assertEqual(len(list_objs), 2)
        self.assertTrue(type(list_objs[0]) is Rectangle)
        self.assertTrue(type(list_objs[1]) is Rectangle)

class TestBase_save_load_squares(unittest.TestCase):
    """Unittests for testing saving and loading of Square objects."""

    def test_save_load_empty_squares(self):
        Square.save_to_file([])
        list_objs = Square.load_from_file()
        self.assertEqual(list_objs, [])

    def test_save_load_squares(self):
        s = Square(2)
        s1 = Square(1)
        Square.save_to_file([s, s1])
        list_objs = Square.load_from_file()
        self.assertTrue(type(list_objs) is list)
        self.assertEqual(len(list_objs), 2)
        self.assertTrue(type(list_objs[0]) is Square)
        self.assertTrue(type(list_objs[1]) is Square)

class TestBase_save_load_json_to_csv(unittest.TestCase):
    """Unittests for testing save_to_file_csv and load_from_file_csv methods."""

    def test_save_load_json_to_csv_empty_list(self):
        Rectangle.save_to_file_csv([])
        list_objs = Rectangle.load_from_file_csv()
        self.assertEqual(list_objs, [])

    def test_save_load_json_to_csv_rectangles(self):
        r = Rectangle(2, 2)
        r1 = Rectangle(1, 1)
        Rectangle.save_to_file_csv([r, r1])
        list_objs = Rectangle.load_from_file_csv()
        self.assertTrue(type(list_objs) is list)
        self.assertEqual(len(list_objs), 2)
        self.assertTrue(type(list_objs[0]) is Rectangle)
        self.assertTrue(type(list_objs[1]) is Rectangle)

    def test_save_load_json_to_csv_squares(self):
        s = Square(2)
        s1 = Square(1)
        Square.save_to_file_csv([s, s1])
        list_objs = Square.load_from_file_csv()
        self.assertTrue(type(list_objs) is list)
        self.assertEqual(len(list_objs), 2)
        self.assertTrue(type(list_objs[0]) is Square)
        self.assertTrue(type(list_objs[1]) is Square)

if __name__ == "__main__":
    unittest.main()
