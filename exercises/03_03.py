#!/usr/bin/env python3

def printLongest(a, b):
    c = len(a) - len(b)

    if c > 0:
        print(a)
    elif c == 0:
        print(a)
        print(b)
    else:
        print(b)

printLongest("123", "1234")
