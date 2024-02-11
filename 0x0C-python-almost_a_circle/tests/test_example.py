#!/usr/bin/python3
"""
Unit test for the Example class.
"""

import unittest
from example import Example

class TestExample(unittest.TestCase):
    """Defines test cases for the Example class."""
    
    def test_get_value(self):
        """Test that get_value method returns the correct value."""
        obj = Example(10)
        self.assertEqual(obj.get_value(), 10)

if __name__ == '__main__':
    unittest.main()
