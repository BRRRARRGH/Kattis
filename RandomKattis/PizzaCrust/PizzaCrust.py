import math

numbers = input().split()
radius = int(numbers[0])
crust = int(numbers[1])

totalArea = radius**2 * math.pi
cheeseArea = (radius - crust)**2 * math.pi

print((cheeseArea / totalArea) * 100)