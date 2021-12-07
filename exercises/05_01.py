#!/usr/bin/env python3

d1 = {1: 1, 2: 2}
d2 = {3: 3, 4: 4}
d3 = {5: 5, 6: 6}

d0 = {}

for d in (d1, d2, d3):
    for (key, value) in (d.keys(), d.values()):
        d0[key] = value

print(d0)
