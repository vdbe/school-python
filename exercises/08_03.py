#!/usr/bin/env python3

import json

data = {"key1": "value1", "key3": "value3", "key2": "value2"}

with open("out.json", "w") as f:
    json.dump(data, f, indent=True)
