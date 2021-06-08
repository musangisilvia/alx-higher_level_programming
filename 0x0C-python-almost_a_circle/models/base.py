#!/usr/bin/python3
"""
    contains a class Base.
"""
import json
import csv


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

    @staticmethod
    def from_json_string(json_string):
        """
            returns the list of the JSON string representation
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            writes the JSON strin representation of list_objs to a file
        """
        fname = cls.__name__ + ".json"
        content = []

        if list_objs is not None:
            for obj in list_objs:
                obj = obj.to_dictionary()
                json_dict = json.loads(cls.to_json_string(obj))
                content.append(json_dict)

        with open(fname, "w") as jfile:
            json.dump(content, jfile)

    @classmethod
    def create(cls, **dictionary):
        """
            returns an instance with all attributes already set.
        """
        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == "Rectangle":
            mod = Rectangle(2, 7)
        elif cls.__name__ == "Square":
            mod = Square(6)
        mod.update(**dictionary)
        return (mod)

    @classmethod
    def load_from_file(cls):
        """
            returns a list of instances
        """
        fname = cls.__name__ + ".json"

        try:
            with open(fname, encoding='utf8') as jfile:
                content = cls.from_json_string(jfile.read())
        except:
            return []

        instances = []

        for instance in content:
            temp = cls.create(**instance)
            instances.append(temp)

        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
            serializes in CSV and saves in a file
        """
        fname = cls.__name__ + ".csv"

        with open(fname, "w", newline='') as cfile:
            writer = csv.writer(cfile)

        if cls.__name__ == "Rectangle":
            for obj in list_objs:
                string = ""
                obj = obj.to_dictionary()
                string += (str(obj["id"]) + "," +
                           str(obj["width"]) + "," +
                           str(obj["height"]) + "," +
                           str(obj["x"]) + "," +
                           str(obj["y"]))
                writer.writerow(string)

        if cls.__name__ == "Square":
            for obj in list_objs:
                string = ""
                obj = obj.to_dictionary()
                string += (str(obj["id"]) + "," +
                           str(obj["width"]) + "," +
                           str(obj["x"]) + "," +
                           str(obj["y"]))
                writer.writerow(string)

    @classmethod
    def load_from_file_csv(cls):
        """
            deserializes from CSV from a file.
        """
        fname = cls.__name__ + ".json"

        try:
            with open(fname, "r") as cfile:
                reader = csv.reader(cfile)
        except:
            return []

        instances = []
        for instance in reader:
            temp = cls.create(**instance)
            instances.append(temp)

        return instances


