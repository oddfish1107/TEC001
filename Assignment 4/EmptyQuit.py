try:
    numList = []
    intnumList = []
    while True:

        number = input("Enter a number: ")
        if number == "":
            print("Program quit")
            break
        numList.append(number)

    for i in numList:
        intnumList.append(i)

    numSort = sorted(intnumList, reverse=True)
    print(numSort)
except:
    print("number pls")