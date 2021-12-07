#!/usr/bin/env python3


def printList():
    l = []
    for ii in range(21):
        l.append(ii * ii)

    print(*l)
    return l


printList()
