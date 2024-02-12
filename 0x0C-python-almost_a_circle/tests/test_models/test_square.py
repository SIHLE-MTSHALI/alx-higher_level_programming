#!/usr/bin/python3
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests for the Square class."""

    def test_square_creation(self):
        """Test creating a Square."""
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_square_str(self):
        """Test the __str__ method for Square."""
        s = Square(3, 1, 3, 10)
        self.assertEqual(str(s), "[Square] (10) 1/3 - 3")

    def test_size(self):
        """Test size getter and setter."""
        s = Square(10)
        self.assertEqual(s.size, 10)
        s.size = 20
        self.assertEqual(s.size, 20)
        with self.assertRaises(TypeError):
            s.size = "size"
        with self.assertRaises(ValueError):
            s.size = -10


class TestSquareUpdate(unittest.TestCase):
    """Tests for Square update method."""

    def test_update_args(self):
        """Test updating Square with *args."""
        s = Square(5)
        s.update(10, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (10) 3/4 - 2")

    def test_update_kwargs(self):
        """Test updating Square with **kwargs."""
        s = Square(5)
        s.update(size=7, id=89, y=1, x=2)
        self.assertEqual(str(s), "[Square] (89) 2/1 - 7")

class TestSquareToDictionary(unittest.TestCase):
    """Test cases for the to_dictionary method of the Square class."""

    def test_to_dictionary(self):
        """Test the dictionary representation of a Square."""
        s = Square(10, 2, 1, 50)
        expected_dict = {'id': 50, 'size': 10, 'x': 2, 'y': 1}
        self.assertEqual(s.to_dictionary(), expected_dict)

if __name__ == "__main__":
    unittest.main()
