#!/usr/bin/env python3


def findCommon(a: list, b: list):
    return set(a) & set(b)


a = ["computer", "mouse", "printer", "safari"]
b = ["safari", "lion", "elephant", "mouse", "rhino"]
print(findCommon(a, b))
