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
        raise AttributeError("area() is not implemented")

    def integer_validator(self, name, value):
        if not type(value) is int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
