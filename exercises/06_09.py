#!/usr/bin/env python3


def f1(s: str):
    return " ".join(
        ["".join(filter(str.isalpha, word))[::-1] for word in s.split()][::-1]
    )

    words = []
    for word in s.split():
        w = "".join(filter(str.isalpha, word))[::-1]
        words.append(w)

    return " ".join(words[::-1])


s = "d32%l+*r53o9W!* o-l=789le%H"
print(f1(s))
