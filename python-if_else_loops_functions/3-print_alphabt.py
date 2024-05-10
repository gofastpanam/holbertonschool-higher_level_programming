#!/usr/bin/python3

for i in range(ord('a'), ord('z') + 1):
    if format(i) != 'e' and format(i) != 'q':
        print("{:c}".format(i), end="")
