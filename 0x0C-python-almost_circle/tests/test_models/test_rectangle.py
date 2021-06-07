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

    def test_rectangle_id(self):
        """
            Testing the id of the rectangle
        """
        r1 = Rectangle(1, 3, 0, 0, 12)
        self.assertEqual(12, r1.id)

    def test_width_str(self):
        """
            Testing wrong type for width: str
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle("w", 5)

    def test_width_list(self):
        """
            Testing wrong type for width: list
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle([1, 2], 8)

    def test_width_bool(self):
        """
            Testing wrong type for width: boolean
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(True, 9)

    def test_height_str(self):
        """
            Testing wrong type for height: str
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(4, "h")

    def test_height_list(self):
        """
            Testing wrong type for height: list
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(8, [1, 2])

    def test_height_bool(self):
        """
            Testing wrong type for height: boolean
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(9, True)

    def test_x_str(self):
        """
            Testing wrong type for x: str
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, "x", 0)

    def test_x_list(self):
        """
            Testing wrong type for x: list
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, [1, 2], 8)

    def test_x_bool(self):
        """
            Testing wrong type for x: boolean
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, True, 9)

    def test_y_str(self):
        """
            Testing wrong type for y: str
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 0, "y")

    def test_y_list(self):
        """
            Testing wrong type for y: list
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 6, [1, 2])

    def test_y_bool(self):
        """
            Testing wrong type for y: boolean
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 9, True)

    def test_width_negative(self):
        """
            Testing negative value for width
        """
        with self.assertRaises(ValueError):
            r1 = Rectangle(-2, 8)

    def test_width_zero(self):
        """
            Testing zero value for width
        """
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 8)

    def test_height_negative(self):
        """
            Testing negative vale fro height
        """
        with self.assertRaises(ValueError):
            r1 = Rectangle(8, -2)

    def test_height_zero(self):
        """
            Testing zero value for height
        """
        with self.assertRaises(ValueError):
            r1 = Rectangle(8, 0)

    def test_x_negative(self):
        """
            Testing negative value for x
        """
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 2, -1, 0)

    def test_y_negative(self):
        """
            Testing negative value for y
        """
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 2, 4, -7)

    def test_area(self):
        """
            Testing the rectangle area
        """
        r1 = Rectangle(12, 2)
        self.assertEqual(r1.area(), 24)

    def test_update_args(self):
        """
            Testing the update function with non-keyword args
        """
        r1 = Rectangle(10, 1)
        r1.update(12)
        self.assertEqual(12, r1.id)

    def test_update_kwargs(self):
        """
            Testing update function with keyword args
        """
        r1 = Rectangle(1, 2)
        r1.update(height=12)
        self.assertEqual(12, r1.height)

    def test_override_str(self):
        """
            Testing override str.
       """
        r1 = Rectangle(1, 2, 3, 4, 76)
        self.assertEqual("[Rectangle] (76) 3/4 - 1/2", r1.__str__())
