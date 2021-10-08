#!/usr/bin/env python3

print("Current date:\t", end="")
c_d, c_m, c_y = map(int, input().split())

print("Date of birth:\t", end="")
b_d, b_m, b_y = map(int, input().split())

y = c_y - b_y


m = c_m - b_m
d = c_d - b_d

if d < 0:
    m -= 1

if m < 0:
    m += 12
    print(m)
    y -= 1


print("Your age is {y} years and {m} months")
