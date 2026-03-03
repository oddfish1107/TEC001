import random

numbers = int(input("Enter the number you want to generate: "))
points_inside_circle = 0
    
for _ in range(numbers):
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)
        
    if (x**2 + y**2) < 1:
        points_inside_circle += 1
            
final_number = 4 * points_inside_circle / numbers
print(final_number)