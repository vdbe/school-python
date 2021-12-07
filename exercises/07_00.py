#!/usr/bin/env python3
import re


def checkSSN(s: str):
    regex = r"(\d{2})\.(\d{2})\.(\d{2})-(\d{3}).(\d{2})"
    return re.match(regex, s) != None


print(checkSSN("00.11.22-345.67"))
print(checkSSN("00112234567"))
