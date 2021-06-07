#!/usr/bin/python3
"""
    contains a class Base.
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            returns JSON string repr of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
