from Lib.http.cookiejar import uppercase_escaped_char
    #unidentified foreign object
try:
    firstLetter = []
    UppercaseLetter = []

    phrase = str(input("Enter a phrase: "))
    phrase = phrase.split()
    for letter in phrase:
        firstLetter.append(letter)
    for x in firstLetter:
        UppercaseLetter.append(x[0])
    StringLetter = "".join(UppercaseLetter).upper()
    print(StringLetter)
except ValueError:
    print("Invalid phrase please try again ")
