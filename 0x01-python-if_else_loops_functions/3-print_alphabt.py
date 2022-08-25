#!/usr/bin/python3
for c in range(97, 123):
    if chr(c) == "q" or chr(c) == "e":
        print("", end="")
    else:
    	print("{:s}".format(chr(c)), end="")
