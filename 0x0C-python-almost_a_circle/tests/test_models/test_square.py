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

if __name__ == "__main__":
    unittest.main()
