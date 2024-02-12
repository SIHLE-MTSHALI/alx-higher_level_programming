#!/usr/bin/python3
"""
Unit tests for the Base class.
"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Define tests for the Base class."""

    @classmethod
    def setUpClass(cls):
        """Method called to prepare the test fixture."""
        Base._Base__nb_objects = 0

    def test_id_assignment(self):
        """Test id assignment with no id and with id."""
        base1 = Base()
        self.assertEqual(base1.id, 1)
        base2 = Base()
        self.assertEqual(base2.id, 2)
        base3 = Base(12)
        self.assertEqual(base3.id, 12)
        base4 = Base()
        self.assertEqual(base4.id, 3)

    def test_id_none(self):
        """Test id assignment with None."""
        base5 = Base(None)
        self.assertEqual(base5.id, 4)

    def test_id_negative(self):
        """Test id assignment with a negative value."""
        base6 = Base(-10)
        self.assertEqual(base6.id, -10)

class TestBaseToJsonString(unittest.TestCase):
    """Test cases for the to_json_string method of the Base class."""

    def test_to_json_string(self):
        """Test JSON string representation of dictionaries."""
        dict_list = [{'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8}]
        json_str = Base.to_json_string(dict_list)
        self.assertEqual(json_str, '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]')

    def test_to_json_string_empty(self):
        """Test JSON string representation with an empty list."""
        self.assertEqual(Base.to_json_string([]), '[]')

    def test_to_json_string_none(self):
        """Test JSON string representation with None."""
        self.assertEqual(Base.to_json_string(None), '[]')

if __name__ == '__main__':
    unittest.main()
