#!/usr/bin/env python3

print("U[V]: ", end="")
U1 = float(input())

print("R1[Ohm]: ", end="")
R1 = float(input())

print("R1[Ohm]: ", end="")
R2 = float(input())

I = U1 / (R1 + R2)
U2 = I * R2

print(f"I = {I:.6f} A, U2 = {U2:.6f} V")
