#!/usr/bin/env python3


def f1(s: str):
    if len(s) < 2:
        return "empty string"

    return s[:2] + s[:-3:-1][::-1]


print(f1("Bananas"))
print(f1("Ba"))
print(f1("B"))
