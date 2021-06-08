"""
    Test Case for task base.py in models directory.
"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """
        Test class for the base class.
    """
    def test_id_none(self):
        """
            initialise an instance of the base class with no id
        """
        b = Base()
        self.assertEqual(1, b.id)

    def test_id(self):
        """
            Initialise an instance with id > 0
        """
        b = Base(12)
        self.assertEqual(12, b.id)

    def test_id_zero(self):
        """
            Initialise instance with id == 0
        """
        b = Base(0)
        self.assertEqual(0, b.id)

    def test_id_negative(self):
        """
            Initialise instance with id < 0
        """
        b = Base(-2)
        self.assertEqual(-2, b.id)

    def test_id_string(self):
        """
            Intialise instance with id is string
        """
        b = Base("Base")
        self.assertEqual("Base", b.id)

    def test_id_list(self):
        """
            Initialise instance with id is list
        """
        b = Base([1, 3, 6])
        self.assertEqual([1, 3, 6], b.id)

    def test_id_tuple(self):
        """
            Initialise instance with id is tuple
        """
        b = Base((1, 3))
        self.assertEqual((1, 3), b.id)

    def test_id_dict(self):
        """
            Initialise instance with id is dict
        """
        b = Base({'id': 12})
        self.assertEqual({'id': 12}, b.id)
