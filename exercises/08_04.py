#!/usr/bin/env python3

import json

with open("out.json", "r") as f:
    data = json.loads(f.read())


print(data["key2"])
