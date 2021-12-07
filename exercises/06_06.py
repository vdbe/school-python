#!/usr/bin/env python3


def f1(s: str):
    l = []
    for c in s:
        if c.isupper():
            l.append(chr((ord(c) + 3 - 65) % 26 + 65))
        else:
            l.append(chr((ord(c) + 3 - 97) % 26 + 97))

    return "".join(l)


print(f1(input("> ")))
