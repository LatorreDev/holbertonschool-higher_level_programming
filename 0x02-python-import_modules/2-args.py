#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 1
    print("{} arguments:".format(len(sys.argv)-1))
    for i in range(len(sys.argv)):
        if i == 0:
            pass
        else:
            print("{:d}: {:}".format(i, (sys.argv[i])))
