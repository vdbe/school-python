#!/usr/bin/env python3


def f1(x: int, y: int):
    l = []
    for ii in range(x):
        l.append([])
        for jj in range(y):
            l[ii].append(ii * jj)
    return l


print(f1(*list(map(int, input("input: ").split(",")))))
