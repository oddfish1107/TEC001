try:
    string = str(input("Enter a string: "))

    if len(string) % 2 == 0:
        middle = len(string)//2
        string = string[middle-1:middle+1]
        print("The middle character is ", string)
    else:
        middle = len(string) // 2
        string = string[middle]
        print("the middle character is ", string)

except:
    print("Invalid type of input please try again")