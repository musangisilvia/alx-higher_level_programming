#!/usr/bin/python


# complex_delete - delets keys with a specific value in a dictionary.
def complex_delete(a_dictionary, value):
    if value in a_dictionary.values():
        for key in a_dictionary.keys():
            if value == a_dictionary[key]:
                del a_dictionary[key]
                break
    return a_dictionary
