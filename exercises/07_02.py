#!/usr/bin/env python3
import re


def snake(s: str):
    regex = re.compile(r".*(python).*", re.IGNORECASE)
    matches = regex.findall(s)
    if len(matches):
        return matches[0]
    else:
        return ""


while True:
    s = input("Text: ").strip()
    if not len(s):
        break

    print(snake(s))
