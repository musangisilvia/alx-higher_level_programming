#!/usr/bin/python3


class Person:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        # print('Hello, my name is', self.name)
        print('Hello, my name is {}'.format(self.name))

# p = Person('Silvia')
# p.say_hi()
Person('Silvia').say_hi()
# line 10 and 11 can be written as Person('Silvia').say_hi()
