#!/usr/bin/python3
"""
    6-base_geometry: class BaseGeometry
"""


class BaseGeometry:
    """
        BaseGeometry
        Attributes: None.
        Methods:
            area() - raises an Exception
            integer_validator() - validates value.
    """
    def area(self):
        """
            Area raise an exception.
	"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            integer_validator checks the value of value.
            Args:
                name (str): name
                value (int): value
	"""
        if not type(value) is int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
