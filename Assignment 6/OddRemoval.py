def odd_remove(list):
    evennum = []
    for number in list:
        if number % 2 == 0:
            evennum.append(number)

    return evennum

mylist = [12, 7, 34, 23, 10, 9, 8, 15]
filtered_list = odd_remove(mylist)
print(f"Original list: {mylist}")
print(f"filtered_list: {filtered_list}")
