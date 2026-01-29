try:
    number_list = []
    while True:

        number = input("Enter a number: ")
        if number == "":
            print("Quit program")
            break
        number_list.append(float(number))


        smallest = min(number_list)
        largest = max(number_list)


    print(f"Smallest number: {smallest}")
    print(f"Largest number: {largest}")



except:
    print("Please enter a number")