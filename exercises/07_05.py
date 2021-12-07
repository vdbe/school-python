#!/usr/bin/env python3
import re

testcases = [
    "johan.vanbauwel@thomasmore.be",
    "johan.van.bauwel@thomasmore.be",
    "info@telenet.BE",
    "duiven.bond@com.com.com",
    "r123456@Student.thomasmore.be",
    "!TEST.be",
    "info@test.belgium",
    "info@!.com",
    "infotest.com",
    "info@test.be$",
    "ET@phone.hom.3",
    "@fundum.be",
]


def maskaddress(s: str):
    s = re.sub(r"\.", "(DOT)", s)
    s = re.sub(r"@", "(AT)", s)
    return s


for email in testcases:
    print(maskaddress(email))
