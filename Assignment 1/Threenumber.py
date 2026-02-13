import math

number1, number2, number3 = map(int, input("Please enter three numbers: ").split())
sum = number1 + number2 + number3
product = number1 * number2
average = sum / 3
print("The sum is",sum)
print("The product is",product)
print("The average is",math.floor(average))

