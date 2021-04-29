#!/usr/bin/python3

import sys

length = len(sys.argv)

if length <= 1:
    print("0 arguments")
elif length == 2:
    print("1 argument:")
    print("1: {:s}".format(sys.argv[1]))
else:
    print("{:d} arguments:".format(length - 1))
    for i in range(1, length):
        print("{:d}: {:s}".format(i, sys.argv[i]))
