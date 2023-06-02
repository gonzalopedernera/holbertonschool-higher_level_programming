#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number > 0:
    ld = number % 10
elif number < 0:
    ld = number % (-10)

if ld == 0:
    str = "and is 0"
elif ld > 5:
    str = "and is greater than 5"
else:
    str = "and is less than 6 and not 0"

print(f"Last digit of {number} is {ld} {str}")
