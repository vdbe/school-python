#!/usr/bin/env python3

print("Input: ", end="")
x = float(input())

if 3 <= x < 8.5:
    print("Condition A true")

if x  < 3 or 5.4 < x <= 7.3 or x > 13:
    print("Condition B true")

if x != 3 and x < 9.75:
    print("Condition C true")
