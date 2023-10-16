#!/usr/bin/python3
"""
Unit tests for the Base class.
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):
    """Test cases for Base class.
    """

    def setUp(self):
        """Set up for tests.
        """
        Base._Base__nb_objects = 0

    def test_base_autoassign_id(self):
        """Test auto-assigned id.
        """
        a = Base()
        self.assertEqual(a.id, 1)

    def test_incrementing_id(self):
        """Test incrementing id.
        """
        a = Base()
        b = Base()
        self.assertEqual(b.id, 2)

    def test_custom_id(self):
        """Test with custom id.
        """
        a = Base(89)
        self.assertEqual(a.id, 89)

    def test_to_json_string(self):
        """Test to_json_string.
        """
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, "[]")
