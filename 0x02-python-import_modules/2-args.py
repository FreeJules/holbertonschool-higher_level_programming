#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    l = len(argv)
    if l == 1:
        print('0 argument.')
    if l == 2:
        print('1 argument:')
        print('1: {:s}'.format(argv[1]))
    if l > 2:
        print('{:d} arguments:'.format(l-1))
        for i in range(1, l):
            print('{:d}: {}'.format(i, argv[i]))
