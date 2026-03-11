nameList = set()
while True:
    name = input("Please enter your name: ")
    if name == '':
        break
    if name in nameList:
        print("That name already exists")
    else:
        print("Please enter a new name")
        nameList.add(name)
print("all the names:")
for name in nameList:
    print(name)