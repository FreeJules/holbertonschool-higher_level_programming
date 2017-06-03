#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""
    with open(filename, mode="w+", encoding="utf-8") as f:
        s = json.dumps(my_obj)
        f.write(s)
