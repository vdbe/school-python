#!/usr/bin/env python3

print("number1: ", end="")
smallest = int(input())

print("number2: ", end="")
num = int(input())

if num < smallest:
    smallest = num

print("number3: ", end="")
num = int(input())

if num < smallest:
    smallest = num


print("number4: ", end="")
num = int(input())

if num < smallest:
    smallest = num


print("number5: ", end="")
num = int(input())

if num < smallest:
    smallest = num

print("the smalles number was", smallest)
