def numberfinder(paragraph):
    total_sum = 0
    current_number_str = ""
    
    for character in paragraph:
        if character.isdigit():
            current_number_str += character
        else:
            if current_number_str != "":
                total_sum += int(current_number_str)
                current_number_str = ""
                
    if current_number_str != "":
        total_sum += int(current_number_str)
        
    return total_sum
print(numberfinder("Today is January 16, 2025. The temperature is 11 degrees Celsius."))