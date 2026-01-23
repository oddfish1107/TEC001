sex = str(input("What is your biological gender (male or female): "))
hemoglobin_level = int(input("How many hemoglobins are there: "))

while sex == "female":
    if 155 > hemoglobin_level > 117:
        print("Normal")
        break
    elif hemoglobin_level < 117:
        print("Low")
        break
    elif hemoglobin_level > 155:
        print("High")
        break
while sex == "male":
    if 167 > hemoglobin_level > 134:
        print("Normal")
        break
    elif hemoglobin_level < 134:
        print("Low")
        break
    elif hemoglobin_level > 167:
        print("High")
        break