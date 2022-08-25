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

# phase 6
print(f"{random.randint(0,999):03d}")
print(str(random.randint(0,9))+ str(random.randint(0,9)) + str(random.randint(0,9)))

# phase 3
length = float(input("Give the length"))
width = float(input("Give the width"))
perimeter = (length + width) *2
area = length * width
print(f"perimeter is {perimeter: .1f}")
print(f"area is {area: .1f}")

# Phase 4
numberone = int(input("Give the integer number 1"))
numbertwo = int(input("Give the integer number 2"))
numberthree = int(input("Give the integer number 3"))
sum = numberone + numbertwo + numberthree
product = numberone*numbertwo*numberthree
average = sum/3
print(sum)
print(product)
print(f"average is {average:.1f}")

# Phase 5
