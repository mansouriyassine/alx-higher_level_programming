#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle

class TestRectangleInstantiation(unittest.TestCase):
    def test_valid_instantiation(self):
        rectangle = Rectangle(10, 2)
        self.assertIsInstance(rectangle, Rectangle)

    def test_invalid_width_type(self):
        with self.assertRaises(TypeError):
            Rectangle("10", 2)

    def test_invalid_height_type(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

    def test_negative_width(self):
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            Rectangle(10, -2)

    def test_zero_width(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_zero_height(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 0)

    def test_valid_x_and_y(self):
        rectangle = Rectangle(10, 2, 3, 4)
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 4)

class TestRectangleArea(unittest.TestCase):
    def test_area_calculation(self):
        rectangle = Rectangle(10, 2)
        self.assertEqual(rectangle.area(), 20)

class TestRectangleStrRepr(unittest.TestCase):
    def test_to_string_representation(self):
        rectangle = Rectangle(10, 2, 3, 4)
        self.assertEqual(str(rectangle), "[Rectangle] (1) 3/4 - 10/2")
        self.assertEqual(repr(rectangle), 'Rectangle(10, 2, 3, 4, 1)')

class TestRectangleUpdate(unittest.TestCase):
    def test_update_args(self):
        rectangle = Rectangle(10, 2, 3, 4)
        rectangle.update(1, 5, 6, 7, 8)
        self.assertEqual(rectangle.id, 1)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 6)
        self.assertEqual(rectangle.x, 7)
        self.assertEqual(rectangle.y, 8)

    def test_update_kwargs(self):
        rectangle = Rectangle(10, 2, 3, 4)
        rectangle.update(width=5, height=6, x=7, y=8)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 6)
        self.assertEqual(rectangle.x, 7)
        self.assertEqual(rectangle.y, 8)

    def test_update_mixed(self):
        rectangle = Rectangle(10, 2, 3, 4)
        rectangle.update(1, width=5, height=6)
        self.assertEqual(rectangle.id, 1)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 6)

class TestRectangleToDictionary(unittest.TestCase):
    def test_to_dictionary(self):
        rectangle = Rectangle(10, 2, 3, 4, 1)
        rect_dict = rectangle.to_dictionary()
        expected_dict = {'id': 1, 'width': 10, 'height': 2, 'x': 3, 'y': 4}
        self.assertEqual(rect_dict, expected_dict)

if __name__ == '__main__':
    unittest.main()
