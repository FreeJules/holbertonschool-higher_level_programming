#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    ld = number % 10
elif number < 0 and number % 10 != 0:
    ld = (10 - (number % 10)) * -1
else:
    ld = 0
if ld > 5:
    print('Last digit of', number, 'is', ld, 'and is greater than 5')
elif ld == 0:
    print('Last digit of', number, 'is', ld, 'and is 0')
elif ld < 6 and ld != 0:
    print('Last digit of', number, 'is', ld, 'and is less than 6 and not 0')
