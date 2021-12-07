#!/usr/bin/env python3
import re


def checkpasswd(s):
    length = r".*.{8}.*"
    upperCase = r".*[A-Z]+.*"
    lowerCase = r".*[a-z]+.*"
    digits = r".*[0-9]+.*"
    speciaChar = r".*[\W\D]{2,}.*"

    restrictions = [length, upperCase, lowerCase, digits, speciaChar]

    for regex in restrictions:
        if re.match(regex, s):
            continue
        else:
            return False

    return True


print(checkpasswd(input("pass: ")))
