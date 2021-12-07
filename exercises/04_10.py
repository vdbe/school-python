#!/usr/bin/env python3

print(*[ii * ii for ii in filter(lambda x: x % 2 == 0, range(1, 21))], sep=", ")
