#!/usr/bin/env python3
from collections import defaultdict
import re
import json

regex = r"^/([a-zA-Z0-9])/([a-zA-Z0-9_-]+)/([a-zA-Z0-9_-]+\.[a-z]+)$"
pattern = re.compile(regex)

d = defaultdict(lambda: 0)

with open("Training_01.txt", "r") as f:
    for line in f.readlines():
        result = pattern.search(line)
        if result != None:
            category = result.group(2)
            d[category] += 1


with open("categories.json", "w") as f:
    json.dump(d, f)
