#!/usr/bin/python3

import random

number = random.randint(-10000, 10000)

last_dig = abs(number) % 10 * (-1 if number < 0 else 1)

print("Last digit of", number, "is", last_dig, "and is", end=" ")

if last_dig > 5:
    print("greater than 5")
elif last_dig == 0:
    print("0")
else:
    print("less than 6 and not 0")
