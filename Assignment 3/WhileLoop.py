def divisiblebythree(num):
    return num % 3 == 0
for num in range(0, 999):
    while divisiblebythree(num):
        print(num)
        break