#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """reads n lines of a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as f:
        lineNum = 1
        while lineNum <= nb_lines or nb_lines <= 0:
            line = f.readline()
            if not line:
                break
            lineNum += 1
            print(line, end='')
