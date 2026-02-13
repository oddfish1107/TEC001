primeNum = int(input("Enter a number "))
while primeNum < 1:
    primeNum = int(input("Enter a number: "))
    print("Prime Number can't be less than 1")
    if primeNum > 1:
        break
if primeNum == 2:
    print("Prime number")
check = True
for i in range(2, int(primeNum**0.5) + 1):
    if primeNum % i == 0:
        print("Not a prime number")
        check = False
if check:
    print("Prime number")