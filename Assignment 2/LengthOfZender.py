length_of_fish = int(input("Enter the length of fish: "))

if length_of_fish <= 41:
    below_the_size_limit = 42 - length_of_fish
    print("Please release the fish because your fish are:" f"{below_the_size_limit} away from the legal size")
else:
    print("Your fish are free to go pal!")