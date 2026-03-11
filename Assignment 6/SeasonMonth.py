months = int(input("Please enter a number of the month(1-12): "))
seasons = ("Winter", "Spring", 'Summer', 'Autumn')
if 1 <= months <= 12:
    true_month = (months % 12) //3
    print(f"Month {months} is {seasons[true_month]}")
else:
    print("Please enter a number between 1 and 12")