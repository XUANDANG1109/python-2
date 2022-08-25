import math
import random

name = "Xuan"
# Now we print the greetings
print("Hello " + name + "!")
print("How it is with you, " + name + "!")
# Phase 1
name = input("what is your name?")
print("Hello, "+name+"!")

# Phase 2
radius = float(input("Give the radius?"))
area = math.pi * radius **2
print("Area is " + str(area))
print(f"Area is {area:.1f}")
print(f"Area is {math.pi* radius **2:.1f}")

