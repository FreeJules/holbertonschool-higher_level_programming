#!/usr/bin/python3
import json


def from_json_string(my_str):
    """returns an object (Python data structure) represented by JSON string"""
    s = json.loads(my_str)
    return (s)
