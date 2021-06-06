"""
    unit test for models/rectangle.py
"""

import unittest
from models.rectangle import Rectangle

r1 = Rectangle(10, 2)
r2 = Rectangle(2, 10)
r3 = Rectangle(10, 2, 1, 1, 12)


class TestRectangle(unittest.TestCase):
    def test_id(self):
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)
