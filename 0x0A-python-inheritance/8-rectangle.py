#!/usr/bin/python3
"""
    8-rectangle: class Rectangle from BaseGeomerty
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        Rectangle inerits from BaseGeometry
        Attributes:
            width (int): width of rectangle.
            height (int): height of rectangle.
        Methods:
            __init__ - initialises the Rectangle.
    """
    def __init__(self, width, height):
        self.integer_validator("Width", width)
        self.integer_validator("Height", height)

        self.__width__ = width
        self.__height__ = height
