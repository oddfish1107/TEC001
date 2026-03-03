def redact_phone_numbers(text):
    result = ""
    origin = 0
    length = len(text)

    while origin < length:
        # Rule 1: Check for "+84" followed by digits
        if text[origin:origin+3] == "+84" and (origin + 3 < length) and text[origin+3].isdigit():
            second_origin = origin + 3
            # Keep moving our 'second_origin' pointer forward as long as we see digits
            while second_origin < length and text[second_origin].isdigit():
                second_origin += 1
            
            result += "[REDACTED]"
            origin = second_origin  # Fast-forward our main loop past the number we just redacted
            continue

        # Rule 2: Check for exactly 10 digits
        if text[origin].isdigit():
            second_origin = origin
            # Keep moving our 'second_origin' pointer forward as long as we see digits
            while second_origin < length and text[second_origin].isdigit():
                second_origin += 1
            
            sequence_length = second_origin - origin
            
            # Ensure it is an isolated 10-digit number (not part of a larger string like A1234567890B)
            is_standalone_start = (origin == 0) or not text[origin-1].isalnum()
            is_standalone_end = (second_origin == length) or not text[second_origin].isalnum()

            if sequence_length == 10 and is_standalone_start and is_standalone_end:
                result += "[REDACTED]"
            else:
                # If it's not exactly 10 digits, keep the original numbers
                result += text[origin:second_origin]  
            
            origin = second_origin
            continue

        # Rule 3: If it is just a normal character or punctuation, add it to the result
        result += text[origin]
        origin += 1

    return result
print(redact_phone_numbers("You may reach Mr. Atkinson through his office number: +842439999999 during work hours, or his cell phone number: 0987654321,"))