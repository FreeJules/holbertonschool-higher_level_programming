#!/usr/bin/python3
def add_attribute(obj, aname, avalue):
    try:
        setattr(obj, aname, avalue)
    except:
        raise TypeError("can't add new attribute")
