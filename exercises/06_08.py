#!/usr/bin/env python3

url = "https://www.youtube.com/watch?v=1vewOUInGv8"
url2 = "https://youtu.be/1vewOUInGv8"


def f1(s: str):
    if s.startswith("https://www.youtube.com/watch?v="):
        return s[len("https://www.youtube.com/watch?v=") :]
    else:
        return s[len("https://youtu.be/") :]


print(f1(url))
print(f1(url2))
