#!/usr/bin/env python3

average = 0

print("Enter integer number: 1: ", end="" )
a = int(input())
average += a
print(f"Average: {average:.2f}")

print("Enter integer number: 2: ", end="" )
a = int(input())
average += a
print(f"Average: {average / 2:.2f}")

print("Enter integer number: 3: ", end="" )
a = int(input())
average += a
print(f"Average: {average / 3:.2f}")

print("Enter integer number: 4: ", end="" )
a = int(input())
average += a
print(f"Average: {average / 4:.2f}")

print("Enter integer number: 5: ", end="" )
a = int(input())
average += a

average /= 5

print(f"Average: {average:.2f}")
