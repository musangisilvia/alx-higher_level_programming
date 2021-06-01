#!/usr/bin/python3
"""
    101-add_attribute: add_attribute()
"""


def add_attribute(cls, name, value):
    """
        adds a new attribute if possible.
    """
    if not hasattr(cls, name):
        cls.name = value
    else:
        raise TypeError("can't add new attribute")
