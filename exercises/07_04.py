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


def checkaddress(s: str):
    regex = r"^[\da-zA-Z\.]+@[a-zA-Z\.]+\.[a-zA-Z]{2,5}$"
    if re.match(regex, s):
        return True
    else:
        return False


for email in testcases:
    print(checkaddress(email))
