try:
    print("Cabin class code available: LUX, A, B, C")
    Cabin_class_code = str(input("Please enter the Cabin class code:"))

    if Cabin_class_code == "LUX":
        print("LUX: upper-deck cabin with a balcony.")
    elif Cabin_class_code == "lux":
        print("LUX: upper-deck cabin with a balcony.")
    elif Cabin_class_code == "A":
        print("A: above the car deck, equipped with a window.")
    elif Cabin_class_code == "a":
        print("A: above the car deck, equipped with a window.")
    elif Cabin_class_code == "B":
        print("B: windowless cabin above the car deck.")
    elif Cabin_class_code == "b":
        print("B: windowless cabin above the car deck.")
    elif Cabin_class_code == "C":
        print("C: windowless cabin below the car deck.")
    elif Cabin_class_code == "c":
        print("C: windowless cabin below the car deck.")
    else:
        print("Invalid cabin class")


except:
    print("DUDE!!! Please enter the character only!")