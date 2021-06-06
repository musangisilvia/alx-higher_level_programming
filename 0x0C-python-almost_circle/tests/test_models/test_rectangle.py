"""
    unit test for models/rectangle.py
"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
        Testing rectangle
    """
    def setUp(self):
        """
            Initialize an insatnce of rectangle.
            With width and height only.
        """
        self.r = Rectangle(20, 10)

    def tearDown(self):
        """
            Deleting created instance
        """
        del self.r

    def test_width(self):
        """
            Testing rectangle width getter
        """
        self.assertEqual(20, self.r.width)

    def test_height(self):
        """
            Testing the height getter
        """
        self.assertEqual(10, self.r.height)

    def test_x(self):
        """
            Testing the x getter
        """
        self.r.x = 2
        self.assertEqual(2, self.r.x)
        self.assertEqual(0, self.r.y)

    def test_y(self):
        """
            Testing the y getter
        """
        self.r.y = 2
        self.assertEqual(2, self.r.y)
        self.assertEqual(0, self.r.x)
