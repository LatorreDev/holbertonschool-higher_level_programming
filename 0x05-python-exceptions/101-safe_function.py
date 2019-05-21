#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        fct(*args)
    except Exception as inst:
        print("Exception: {}".format(inst), file=sys.stderr)
        return None
