#!/usr/bin/env python3
import random

with open("randomadd.txt", "a") as f:
    f.write(str(random.randint(0, 9)))
