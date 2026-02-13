def listofintegers(list):
    sorted_even = sorted([num for num in list if num % 2 == 0])
    return sorted_even
intlist = [1,2,3,4,5,6,7,8,9]
print(intlist)
print(listofintegers(intlist))
