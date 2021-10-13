#!/usr/bin/env python3

def f1(a: int):
    try:
        return 45 / a
    except ZeroDivisionError:
        return 0

print(f1(0))
