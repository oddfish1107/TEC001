talents, pounds, iots = map(float, input('What is your talents, pounds, and Iots:').split())
pounds = (pounds + talents * 20)
iots = (32 * pounds + iots)
grams = 13.3 * iots
kilograms = grams / 1000
gram = grams % 1000
print(f"The weight in modern units:{int(kilograms)} kilograms and {round(gram,2)} grams")