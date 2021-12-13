#!/usr/bin/env python3

import json
import csv

with open("out.json", "r") as f:
    data = json.loads(f.read())

l = []

for key, value in zip(data.keys(), data.values()):
    l.append((key, value))

l.sort()

with open("keys.csv", "w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=",")
    for row in l:
        csv_writer.writerow(row)
