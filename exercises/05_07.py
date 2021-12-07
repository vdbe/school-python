#!/usr/bin/env python3


def merge(keys: list, values: list):
    d = {}
    for (key, value) in zip(keys, values):
        d[key] = values

    return d


cities = ["Antwerpen", "Lier", "Mechelen", "Brussel"]
postalCodes = [2000, 2500, 2800, 1000]
print(merge(cities, postalCodes))
