#!/usr/bin/python3
def number_of_lines(filename=""):
    """counts number of lines"""
    with open(filename, mode="r", encoding="utf-8") as f:
        lineNum = 0
        for line in f:
            lineNum += 1
    return (lineNum)
