#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {0:d} is".format(number), end="")
if number < 0:
    number = number * -1
    number = number % 10
    number = number * -1
else:
    number = number % 10
if number > 5:
    print(" {0:d} and is greater than 5".format(number))
elif number == 0:
    print(" {0:d} and is {0:d}".format(number))
elif number < 6:
    print(" {0:d} and is less than 6 and not 0".format(number))
