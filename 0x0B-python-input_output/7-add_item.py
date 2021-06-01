#!/usr/bin/python3
"""
    This is a python script that adds all arguments to a Python List.
    List is then saved to a file.
"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    arg_list = []
    filename = "add_item.json"
    for arg in sys.argv:
        arg_list.append(arg)
    arg_list.pop(0)
    save_to_json_file(arg_list, filename)
    load_from_json_file(filename)
