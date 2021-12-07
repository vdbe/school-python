#!/usr/bin/env python3
import re


def maskCC(s: str):
    regex = r"(\d{4})[ -]?(\d{4})[ -]?(\d{4})[ -]?(\d{4})"
    mo = re.search(regex, s)
    return " ".join(["XXXX"] * 3 + [mo[4]])


print(maskCC("1234567812345678"))
print(maskCC("1234 5678 1234 5678"))
print(maskCC("1234-5678-1234-5678"))
print(maskCC("1234 5678-12345678"))
