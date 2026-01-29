
try:
    inches = int(input("Enter an inch to convert: "))
    while inches > 0:
     centimeters = inches * 2.54
     print(f"{inches} = {centimeters} centimeters")
     inches = int(input("Enter an inch to convert: "))
     if inches < 0:
        print("Inches cannot be negative")
        break
except:
    print("Please enter a valid inch")




