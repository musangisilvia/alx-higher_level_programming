#!/usr/bin/python3


class User:
    id = 89
    name = "no_name"
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name

u = User()
# u.is_new
# type(u.is_new)
u.id
u = User('Silvia')
u.name
