#!/usr/bin/python3
def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8)"""
    """returns the number of characters added"""
    with open(filename, mode="a+", encoding="utf-8") as f:
        chars = f.write(text)
    return chars
