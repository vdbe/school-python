#!/usr/bin/env python3

l = [1, 2, 3, 4, 5, 6, 7, 8]
print(*l, sep="\n")
[print(a) for a in l]

for element in l:
    print(element)
