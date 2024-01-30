#!/usr/bin/python3
"""Unittest for max_integer([..])."""
import unittest
from 6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    """Defines test cases for the max_integer function."""

    def test_ordered_list(self):
        """Test with an ordered list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list."""
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_single_element(self):
        """Test with a list of a single element."""
        self.assertEqual(max_integer([1]), 1)

    def test_negative_numbers(self):
        """Test with a list containing negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_none(self):
        """Test with None as input."""
        with self.assertRaises(TypeError):
            max_integer(None)

if __name__ == '__main__':
    unittest.main()
