import math

length, width = map(float, input("What is the length and width? ").split())

area = length * width
perimeter = 2 * (length + width)

print("The perimeter of the circle is:",math.floor(perimeter))
print("The area of the circle is:",math.floor(area))