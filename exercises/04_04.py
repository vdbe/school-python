#!/usr/bin/env python3

values = []
for ii in range(5):
    values.extend(map(str.strip, input(f"line {ii}: ").split(",")))

values.sort(key=str.lower)

print(values)
