#!/usr/bin/env python3


def tagMe(inner: str, tag: str):
    print(f"<{tag}>{inner}</{tag}>")


tagMe("Python", "i")
tagMe("Python", "b")
