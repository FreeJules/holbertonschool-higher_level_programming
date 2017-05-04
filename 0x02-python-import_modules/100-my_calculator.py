#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    l = len(argv)
    if l != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    if len(argv[2]) != 1:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
a = int(argv[1])
b = int(argv[3])
c = argv[2]
if c == '+':
    print('{:d} {:s} {:d} = {:d}'.format(a, c, b, add(a, b)))
elif c == '-':
    print('{:d} {:s} {:d} = {:d}'.format(a, c, b, sub(a, b)))
elif c == '*':
    print('{:d} {:s} {:d} = {:d}'.format(a, c, b, mul(a, b)))
elif c == '/':
    print('{:d} {:s} {:d} = {:d}'.format(a, c, b, div(a, b)))
else:
    print('Unknown operator. Available operators: +, -, * and /')
    exit(1)
