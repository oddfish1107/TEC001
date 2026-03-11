def main():

    numberlist = []
    while True:
        number = input("Enter a number: ")
        if number == '':
            break
        try:
            numbers = float(number)
            numberlist.append(numbers)
        except ValueError:
            print("Please enter a number")
    numberlist.sort(reverse=True)
    five = numberlist[:5]

    print('the greatest number is:')
    for num in five:
        if num.is_integer():
            print(int(num))
        else:
            print(num)
if __name__ == '__main__':
    main()

