#!/usr/bin/env python3

print("Start time:\t", end="")
start_h, start_m, start_s = map(int, input().split())

print("Stop timeh:\t", end="")
stop_h, stop_m, stop_s = map(int, input().split())

h = stop_h - start_h
m = stop_m - start_m
s = stop_s - start_s

if s < 0:
    s += 60
    m -= 1

if m < 0:
    m += 60
    h -= 1

if h < 0:
    h += 24

print("Difference: ", h, m, s)
