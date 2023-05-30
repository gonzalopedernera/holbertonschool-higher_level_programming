#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number > 0):
    ld = number % 10
elif (number < 0):
    ld = (number * -1) % 10

print(f"Last digit of {number} is {ld} ", end="")

if (ld == 0):
    print("and is 0", end="")
elif (ld > 5):
    print("and is greater than 5 ", end="")
elif (ld < 6):
    print("and is less than 6 ", end="")

if (ld != 0):
    print("and is not 0", end="")

print("")
