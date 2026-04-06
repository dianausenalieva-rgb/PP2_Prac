#1
import math

degree = float(input("Enter degree: "))
radian = degree * (math.pi / 180)

print("Radian:", radian)
#2
base1 = float(input("Enter first base: "))
base2 = float(input("Enter second base: "))
height = float(input("Enter height: "))

area = 0.5 * (base1 + base2) * height

print("Area of trapezoid:", area)
#3
import math

n = int(input("Enter number of sides: "))
s = float(input("Enter length of a side: "))

area = (n * s ** 2) / (4 * math.tan(math.pi / n))

print("Area of regular polygon:", area)
#4
base = float(input("Enter base: "))
height = float(input("Enter height: "))

area = base * height

print("Area of parallelogram:", area)