#!/usr/bin/python3
"""
    contains a class Base.
"""


class Base:
    """
        base class for the entire project.
        Attributes:
            __nb_ojects (int)
            id (int)
        Methods:
            __init__()
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
           Initializes the class attributes.
           Args:
               id (int)
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
