import random
try:
    four_digits = ''
    three_digit = random.randint(100, 999)
    print("The random number is",three_digit)
    while len(four_digits) < 4:

        four_digits += str(random.randint(1, 6))

    print("The random number is",four_digits)


except:
    number = 1
    print("NO")


