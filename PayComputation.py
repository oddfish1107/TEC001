
try:
    hours = int(input("Enter Hours:"))
    rate = int(input("Enter Rate:"))

    if hours > 40:
        total_pay = (40 * rate) + ((hours - 40) * rate *1.5)
        print(total_pay)
    else:
        total_pay = hours * rate


except:
    print('Error, please enter numeric input')