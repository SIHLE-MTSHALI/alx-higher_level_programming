#!/usr/bin/python3
"""
Unit tests for the Rectangle class.
"""
import io
from contextlib import redirect_stdout
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
    
    def test_area(self):
        """Test the area calculation of the rectangle."""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)
   
    def test_display(self):
        """Test the display method."""
        r1 = Rectangle(4, 6)
        expected_output = "####\n" * 6
        with io.StringIO() as buf, redirect_stdout(buf):
            r1.display()
            self.assertEqual(buf.getvalue(), expected_output)

    def test_str_method(self):
        """Test the __str__ method of the Rectangle class."""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")
        r2 = Rectangle(5, 5, 1)
        expected_id = 8
        self.assertEqual(str(r2), f"[Rectangle] ({expected_id}) 1/0 - 5/5")

if __name__ == '__main__':
    unittest.main()
