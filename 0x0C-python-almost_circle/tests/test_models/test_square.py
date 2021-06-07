"""
    unit test for models/square.py
"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """
        Testing square
    """
    def setUp(self):
        """
            Initialize an insatnce of square
            With size only
        """
        self.sq = Square(20)

    def tearDown(self):
        """
            Deleting created instance
        """
        del self.sq

    def test_size(self):
        """
            Testing square size getter
        """
        self.assertEqual(20, self.sq.width)

    def test_x(self):
        """
            Testing the x getter
        """
        self.sq.x = 2
        self.assertEqual(2, self.sq.x)
        self.assertEqual(0, self.sq.y)

    def test_y(self):
        """
            Testing the y getter
        """
        self.sq.y = 2
        self.assertEqual(2, self.sq.y)
        self.assertEqual(0, self.sq.x)

    def test_square_id(self):
        """
            Testing the id of the square
        """
        sq1 = Square(1, 0, 0, 12)
        self.assertEqual(12, sq1.id)

    def test_size_str(self):
        """
            Testing wrong type for size: str
        """
        with self.assertRaises(TypeError):
            sq1 = Square("s")

    def test_size_list(self):
        """
            Testing wrong type for size: list
        """
        with self.assertRaises(TypeError):
            sq1 = Square([1, 2])

    def test_size_bool(self):
        """
            Testing wrong type for size: boolean
        """
        with self.assertRaises(TypeError):
            sq1 = Square(True)

    def test_x_str(self):
        """
            Testing wrong type for x: str
        """
        with self.assertRaises(TypeError):
            sq1 = Square(2, "x", 0)

    def test_x_list(self):
        """
            Testing wrong type for x: list
        """
        with self.assertRaises(TypeError):
            sq1 = Square(2, [1, 2], 8)

    def test_x_bool(self):
        """
            Testing wrong type for x: boolean
        """
        with self.assertRaises(TypeError):
            sq1 = Square(2, True, 9)

    def test_y_str(self):
        """
            Testing wrong type for y: str
        """
        with self.assertRaises(TypeError):
            sq1 = Square(2, 0, "y")

    def test_y_list(self):
        """
            Testing wrong type for y: list
        """
        with self.assertRaises(TypeError):
            sq1 = Square(2, 6, [1, 2])

    def test_y_bool(self):
        """
            Testing wrong type for y: boolean
        """
        with self.assertRaises(TypeError):
            sq1 = Square(2, 9, True)

    def test_size_negative(self):
        """
            Testing negative value for size
        """
        with self.assertRaises(ValueError):
            sq1 = Square(-2)

    def test_size_zero(self):
        """
            Testing zero value for size
        """
        with self.assertRaises(ValueError):
            sq1 = Square(0)

    def test_x_negative(self):
        """
            Testing negative value for x
        """
        with self.assertRaises(ValueError):
            sq1 = Square(2, -1, 0)

    def test_y_negative(self):
        """
            Testing negative value for y
        """
        with self.assertRaises(ValueError):
            sq1 = Square(2, 4, -7)
