
# Phase 1
name = input("what is your name?")
print("Hello, " + name + "!")

# Phase 2
radius = float(input("Give the radius?"))
area = math.pi * radius ** 2
print("Area is " + str(area))
print(f"Area is {area:.1f}")
print(f"Area is {math.pi * radius ** 2:.1f}")

# phase 3
length = float(input("Give the length"))
width = float(input("Give the width"))
perimeter = (length + width) * 2
area = length * width
print(f"perimeter is {perimeter: .1f}")
print(f"area is {area: .1f}")

# Phase 4
numberone = int(input("Give the integer number 1"))
numbertwo = int(input("Give the integer number 2"))
numberthree = int(input("Give the integer number 3"))
sum = numberone + numbertwo + numberthree
product = numberone * numbertwo * numberthree
average = sum / 3
print(sum)
print(product)
print(f"average is {average:.1f}")

# Phase 5
convert_talent = float(input("Enter talent to convert into kilograms:"))
convert_pounds = float(input("Enter pounds to convert into kilograms:"))
convert_lot = float(input("Enter lot to convert into kilograms:"))
talent = 20 * convert_talent * 32 * 13.3
pounds = 32 * convert_pounds *13.3
lot = 13.3 * convert_lot
sum_gram = talent + pounds + lot
result_kg = int(sum_gram // 1000)
result_gram = float(sum_gram % 1000)
print("The weight in modern units:",result_kg, f"kilograms and, {result_gram:.2f} grams")

# Phase 6
#a
print(f"{random.randint(0, 999):03d}")
print(str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)))

#b
print(str(random.randint(1, 6)) + str(random.randint(1, 6)) + str(random.randint(1, 6)) + str(random.randint(1, 6)))