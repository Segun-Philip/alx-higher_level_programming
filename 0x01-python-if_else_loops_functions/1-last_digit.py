#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
value = abs(number) % 10
if number < 0:
    value = -(value)
print(f"Last digit of {number} is {value} and is ", end="")
if value > 5:
    print("greater than 5")
elif value == 0:
    print("0")
else:
    print("less than 6 and not 0")
