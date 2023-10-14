#!/usr/bin/python3
"""Defines unittests for base.py.

Unittest classes:
    TestBase_instantiation - Test instantiation of the Base class.
    TestBase_to_json_string - Test the to_json_string method.
    TestBase_save_to_file - Test the save_to_file method.
    TestBase_from_json_string - Test the from_json_string method.
    TestBase_create - Test the create method.
    TestBase_load_from_file - Test the load_from_file method.
    TestBase_save_to_file_csv - Test the save_to_file_csv method.
    TestBase_load_from_file_csv - Test the load_from_file_csv method.
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_nb_instances_after_unique_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_id_public(self):
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_str_id(self):
        self.assertEqual("hello", Base("hello").id)

    def test_float_id(self):
        self.assertEqual(5.5, Base(5.5).id)

    def test_complex_id(self):
        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_dict_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_frozenset_id(self):
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def test_range_id(self):
        self.assertEqual(range(5), Base(range(5)).id)

    def test_bytes_id(self):
        self.assertEqual(b'Python', Base(b'Python').id)

    def test_bytearray_id(self):
        self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).id)

    def test_memoryview_id(self):
        self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).id)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBase_to_json_string(unittest.TestCase):
    """Unittests for testing to_json_string method of Base class."""

    def test_to_json_string_rectangle_type(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()]))

    def test_to_json_string_rectangle_one_dict(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)

    def test_to_json_string_rectangle_two_dicts(self):
        r1 = Rectangle(2, 3, 5, 19, 2)
        r2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    def test_to_json_string_square_type(self):
        s = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()]))

    def test_to_json_string_square_one_dict(self):
        s = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([s.to_dictionary()])) == 39)

    def test_to_json_string_square_two_dicts(self):
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


class TestBase_save_to_file(unittest.TestCase):
    """Unittests for testing save_to_file method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_one_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_to_file_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105)

    def test_save_to_file_one_square(self):
        s = Square(10, 2, 3, 4)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_two_squares(self):
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 77)

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Base.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.save_to_file([], 1)

    def test_save_to_file_incorrect_file_arg(self):
        with self.assertRaises(FileNotFoundError):
            Base.save_to_file([], '/wrong/path')

    def test_save_to_file_empty_list(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 2)
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 2)
        Base.save_to_file([])
        with open("Base.json", "r") as f:
            self.assertTrue(len(f.read()) == 2)


class TestBase_from_json_string(unittest.TestCase):
    """Unittests for testing from_json_string method of Base class."""

    def test_from_json_string_empty_string(self):
        self.assertEqual([], Base.from_json_string(""))

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_one_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        list_input = [r.to_dictionary()]
        self.assertEqual(list_input, Base.from_json_string(Base.to_json_string(list_input)))

    def test_from_json_string_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        list_input = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertEqual(list_input, Base.from_json_string(Base.to_json_string(list_input)))

    def test_from_json_string_one_square(self):
        s = Square(10, 2, 3, 4)
        list_input = [s.to_dictionary()]
        self.assertEqual(list_input, Base.from_json_string(Base.to_json_string(list_input)))

    def test_from_json_string_two_squares(self):
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        list_input = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertEqual(list_input, Base.from_json_string(Base.to_json_string(list_input)))

    def test_from_json_string_one_rectangle_and_one_square(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        s1 = Square(10, 2, 3, 4)
        list_input = [r1.to_dictionary(), s1.to_dictionary()]
        self.assertEqual(list_input, Base.from_json_string(Base.to_json_string(list_input)))

    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)


class TestBase_create(unittest.TestCase):
    """Unittests for testing create method of Base class."""

    def test_create_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 6)
        r_dict = r.to_dictionary()
        r2 = Rectangle.create(**r_dict)
        self.assertNotEqual(r, r2)
        self.assertNotEqual(r is r2, True)
        self.assertEqual(type(r) is type(r2), True)

    def test_create_square(self):
        s = Square(10, 7, 2, 8)
        s_dict = s.to_dictionary()
        s2 = Square.create(**s_dict)
        self.assertNotEqual(s, s2)
        self.assertNotEqual(s is s2, True)
        self.assertEqual(type(s) is type(s2), True)

    def test_create_no_args(self):
        with self.assertRaises(TypeError):
            Base.create()

    def test_create_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.create(1, 2)


class TestBase_load_from_file(unittest.TestCase):
    """Unittests for testing load_from_file method of Base class."""

    def test_load_from_file_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        list_input = [r1, r2]
        Rectangle.save_to_file(list_input)
        list_output = Rectangle.load_from_file()
        self.assertEqual(list_input, list_output)

    def test_load_from_file_squares(self):
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        list_input = [s1, s2]
        Square.save_to_file(list_input)
        list_output = Square.load_from_file()
        self.assertEqual(list_input, list_output)

    def test_load_from_file_empty_file(self):
        list_output = Square.load_from_file()
        self.assertEqual(list_output, [])

    def test_load_from_file_no_args(self):
        with self.assertRaises(TypeError):
            Base.load_from_file()

    def test_load_from_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file(1, 2)


class TestBase_save_to_file_csv(unittest.TestCase):
    """Unittests for testing save_to_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_save_to_file_csv_one_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file_csv([r])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue(len(f.read()) == 37)

    def test_save_to_file_csv_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue(len(f.read()) == 71)

    def test_save_to_file_csv_one_square(self):
        s = Square(10, 2, 3, 4)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue(len(f.read()) == 25)

    def test_save_to_file_csv_two_squares(self):
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        Square.save_to_file_csv([s1, s2])
        with open("Square.csv", "r") as f:
            self.assertTrue(len(f.read()) == 49)

    def test_save_to_file_csv_no_args(self):
        with self.assertRaises(TypeError):
            Base.save_to_file_csv()

    def test_save_to_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.save_to_file_csv([], 1)

    def test_save_to_file_csv_incorrect_file_arg(self):
        with self.assertRaises(FileNotFoundError):
            Base.save_to_file_csv([], '/wrong/path')


class TestBase_load_from_file_csv(unittest.TestCase):
    """Unittests for testing load_from_file_csv method of Base class."""

    def test_load_from_file_csv_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        list_input = [r1, r2]
        Rectangle.save_to_file_csv(list_input)
        list_output = Rectangle.load_from_file_csv()
        self.assertEqual(list_input, list_output)

    def test_load_from_file_csv_squares(self):
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        list_input = [s1, s2]
        Square.save_to_file_csv(list_input)
        list_output = Square.load_from_file_csv()
        self.assertEqual(list_input, list_output)

    def test_load_from_file_csv_empty_file(self):
        list_output = Square.load_from_file_csv()
        self.assertEqual(list_output, [])

    def test_load_from_file_csv_no_args(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv()

    def test_load_from_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv(1, 2)


if __name__ == "__main__":
    unittest.main()
