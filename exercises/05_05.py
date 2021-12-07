#!/usr/bin/env python3
students = {
    "id1": {"name": "Tom", "gender": "M", "courses": "dsp, math, python"},
    "id2": {
        "name": "Alice",
        "gender": "F",
        "courses": "operating systems, math, python",
    },
    "id3": {"name": "Tom", "gender": "M", "courses": "dsp, math, python"},
    "id4": {"name": "Bob", "gender": "M", "courses": "math, python"},
}


to_be_removed = []
for (ii, (key, value)) in enumerate(zip(students.keys(), students.values())):
    index = list(students.values()).index(value)
    if index < ii:
        to_be_removed.append(key)
for key in to_be_removed:
    del students[key]

for k in students.keys():
    print(k, students[k])
