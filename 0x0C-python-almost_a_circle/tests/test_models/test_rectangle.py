#!/usr/bin/python3
"""
Unit tests for the Rectangle class.
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Define tests for the Rectangle class."""

    def test_width_height_type_validation(self):
        """Test that width and height must be integers."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")

    def test_width_height_value_validation(self):
        """Test width and height values must be greater than zero."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -2)

    def test_x_y_type_validation(self):
        """Test that x and y must be integers."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, "0", 0)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 0, "0")

    def test_x_y_value_validation(self):
        """Test x and y values must be greater than or equal to zero."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -1, 0)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 0, -1)

if __name__ == '__main__':
    unittest.main()
