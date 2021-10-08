#!/usr/bin/env python3

print("int: ", end="" )
num = int(input())

s = 0
for i in range(1, num + 1):
    s += i
print(s)
