#!/usr/bin/env python3


def printList(start: int, stop: int):
    l = []
    for ii in range(start, stop + 1):
        l.append(ii * ii)

    print(tuple(l))
    return l


printList(3, 7)
