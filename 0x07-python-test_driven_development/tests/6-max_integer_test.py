#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        """Test an empty list."""
        self.assertIsNone(max_integer([]))

    def test_max_integer(self):
        """Test a list with maximum integer."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_integers(self):
        """Test a list with negative integers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_integers(self):
        """Test a list with mixed positive and negative integers."""
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)

    def test_single_integer(self):
        """Test a list with a single integer."""
        self.assertEqual(max_integer([42]), 42)

if __name__ == '__main__':
    unittest.main()
