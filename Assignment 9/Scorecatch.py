def score(filename):
    totalscore = 0
    students = 0
    try:
        with open(filename, "r", encoding='utf-8') as f:
            for line in f:
                seperate = line.strip().split(',')
                if len(seperate) == 2:
                    name = seperate[0]
                    score_str = seperate[1]
                    try:
                        scorefloat = float(score_str)
                        totalscore += scorefloat
                        students += 1
                    except ValueError:
                        print(f"Warning: Could not understand the score for {filename}. Skipping.")
                else:
                    print(f"Warning: Could not understand the score for {filename}. Skipping.")
            if students == 0:
                return 0
            average = totalscore / students
            return average

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    return None
print(score("text.txt"))