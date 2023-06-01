#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("1 argument:\n1: {}".format(sys.argv[1]))
    elif len(sys.argv) > 2:
        argnum = len(sys.argv)
        print("{} arguments:".format(argnum - 1))
        for i in range(1, argnum):
            print("{}: {}".format(i, sys.argv[i]))
