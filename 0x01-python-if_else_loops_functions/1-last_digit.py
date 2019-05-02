#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

print("Last digit of {0:d} is".format(number))

number = number%10
if number % 10 > 5:
    print(" {0:d} and is greater than 5".format(number))
elif number % 10 == 0:
    print(" 0 and is 0")
elif number % 10 < 6:
    print(" {0:d} and is less than 6 and not 0".format(number))
