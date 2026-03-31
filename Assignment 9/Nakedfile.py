def linecount(filename):
    try:
        countlines = open(filename,"r")
        count = 0
        for _ in countlines:
            count += 1
        print('line Count: ', count)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
linecount("text.txt")