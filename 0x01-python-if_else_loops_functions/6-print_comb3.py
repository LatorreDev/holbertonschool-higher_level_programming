#!/usr/bin/python3
for a in range(10):
    for b in range(10):
        if a == 8 and b == 9:
            print("{0:d}{1:d}".format(a, b))
        elif a < b:
            print("{0:d}{1:d}, ".format(a, b), end='')
