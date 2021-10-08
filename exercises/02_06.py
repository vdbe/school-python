#!/usr/bin/env python3

print("Enter your speed:\t", end="")
speed = float(input())
print("Enter speed limit:\t", end="")
limit = float(input())

if speed > limit:
    fine = min(100, (speed - limit) * 2.5)
    print(f"You were speeding {speed - limit:.0f}km/h and have to pay {fine:.2f}")
else:
    print("You are good")
