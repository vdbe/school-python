#!/usr/bin/env python3

data = {
    "name": "Alice",
    "age": 20,
    "courses": [{"name": "Python", "SP": 6}, {"name": "DSP", "SP": 6}],
}


class Course:
    def __init__(self, name: str, sp: int):
        super().__init__()
        self.name = name
        self.sp = sp


class Student:
    def __init__(self, name: str, age: int, courses: list):
        super().__init__()
        self.age = age
        self.name = name
        self.courses = courses
