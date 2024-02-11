#!/usr/bin/python3
"""
Unit tests for the Rectangle class.
"""
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Define tests for the Rectangle class."""

    def test_rectangle_creation(self):
        """Test normal creation of a rectangle."""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_rectangle_id(self):
        """Test rectangle id assignment."""
        r2 = Rectangle(2, 10, 0, 0, 98)
        self.assertEqual(r2.id, 98)

    # Add more tests as needed

if __name__ == '__main__':
    unittest.main()
