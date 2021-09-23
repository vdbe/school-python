#!/usr/bin/env python3

print("Input: ", end="")
a, b = map(int, input().split())

print(f"Sum: {a + b}")
print(f"Product: {a * b}")
print(f"Integer quotient: {a // b}")
print(f"Quotient: {a / b}")
print(f"Quotient (2 decimal places): {a / b:.2f}")
print(f"Remainder: {a % b}")
