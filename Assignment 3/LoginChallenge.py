try:
    access_limit = 5
    while True:

        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        if username == "python" and password == "rule":
            print("Welcome")
        else:
            print("Invalid username or password please try again")
            access_limit = access_limit - 1
            print("you have" f" {access_limit} " "times left")
            if access_limit == 0:
                print("Access denied")
                break
except :
    print("Invalid username or password please try again")

