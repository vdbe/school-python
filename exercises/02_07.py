#!/usr/bin/env python3

print("weight in kg: ", end="")
weight = float(input())

print("size in m: ", end="")
size = float(input())

bmi = weight/size**2

if bmi < 20:
    print("normal weight")
elif bmi > 25:
    print("overweighed")
else:
    print("ideal weight")

print(bmi)
