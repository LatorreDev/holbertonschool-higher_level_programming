#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        j = chr(ord(str[i]) - 32) \
            if (ord(str[i]) > 96 and ord(str[i]) < 123) \
            else str[i]
        print('{}'.format(j), end="")
    print()
