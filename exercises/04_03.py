#!/usr/bin/env python3


def removeFromList(l: list, s: str):
    orig_size = len(l)
    l[:] = list(filter(lambda element: element != s, l))
    return orig_size - len(l)


spam = ["cat", "bat", "rat", "cat", "hat", "cat"]
print(removeFromList(spam, "cat"), "entries deleted")
print(spam)
