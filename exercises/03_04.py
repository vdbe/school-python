#!/usr/bin/env python3

def printOddEven(a):
    b = ["even", "odd"]
    print(f"{a} is {b[a%2]}")


printOddEven(2)
