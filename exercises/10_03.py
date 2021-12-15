#!/usr/bin/env python3
import math

# import sympy.ntheory as nt


class MyNumber:
    def __init__(self, n: int):
        self.n = n

    def sum(self):
        return sum(range(1, self.n + 1))

    def factorial(self):
        return math.factorial(self.n)

    def isprime(self):
        # return nt.isprime(self.n)
        # TODO: Wirte a prime checker
        return False


nr = MyNumber(5)
print(nr.sum())
print(nr.factorial())
print(nr.isprime())
