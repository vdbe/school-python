#!/usr/bin/env python3

d1 = {"a": 10, "b": 20, "c": 30}
d2 = {"a": 30, "b": 20, "d": 40}

d3 = d1.copy()

d3.update()
for (key, value) in zip(d2.keys(), d2.values()):
    if key in d3:
        d3[key] += value
    else:
        d3[key] = value

print(d3)
