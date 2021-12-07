#!/usr/bin/env python3

l = []
for ii in range(5):
    n = int(input(f"Int {ii}: "))
    l.append(n)
    l.sort()
    print(l)
