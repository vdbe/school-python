#!/usr/bin/env python3

SECOND = 1
MINUTE = SECOND * 60
HOUR = MINUTE * 60
DAY = HOUR * 24

print("seconds: ", end="" )
seconds = int(input())

days = seconds // DAY
seconds -= days * DAY

hours = seconds // HOUR
seconds -= hours * HOUR

minutes = seconds // MINUTE
seconds -= minutes * MINUTE

print(f"Time is {days} days, {hours} hours, minutes {minutes}, {seconds} seconds")
