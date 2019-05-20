#!/usr/bin/python3
def safe_print_division(a, b):
    my_division = 0
    try:
        my_division = a / b
    except ZeroDivisionError:
        my_division = None
        return None
    finally:
        print("Inside result: {}".format(my_division))
    return my_division
