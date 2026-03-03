try:
    
    def university_code(code):
        if len(code) not in [5, 6]:
            return False
        letters = code[:-3]
        digits = code[-3:]
        if not (letters.isalpha() and letters.isupper()):
            return False
        if not digits.isdigit():
            return False
        return True
    print(university_code(input("Enter your university code: ")))


except:
    print("Wrong")