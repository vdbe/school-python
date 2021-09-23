#!/usr/bin/env python3

# Input
print("Money: ", end="")
ones = int(input())

# Output
print(f"500: {ones // 500}")
ones %= 500;

print(f"200: {ones // 200}")
ones %= 200

print(f"100: {ones // 100}")
ones %= 100

print(f"50: {ones // 50}")
ones %= 50

print(f"20: {ones // 20}")
ones %= 20

print(f"10: {ones // 10}")
ones %= 10

print(f"5: {ones // 5}")
ones %= 5

print(f"2: {ones // 2}")
ones %= 2

print(f"1: {ones}")

