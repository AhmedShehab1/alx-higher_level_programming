#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
temp = number
if temp < 0:
	temp *= -1
print(f"Last digit of {number} is {temp % 10}", end=" ")
if temp % 10 > 5:
    print("and is greater than 5")
elif temp % 10 < 6 and temp % 10 != 0:
    print("and is less than 6 and not 0")
elif temp % 10 == 0:
    print("and is 0")
