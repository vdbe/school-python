#!/usr/bin/env python3

def fact(a: int):
    ret = 1
    for i in range(1, a+1):
        ret *= i

    return ret

print(fact(5))
