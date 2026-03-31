def ceaser_cipher(filename,shift,direction):

    with open(filename, "r") as f:
        text = f.read()
    cipher = ""
    for word in text:
        if word.isalpha():
            if word.isupper():
                base = 65
            else:
                base = 97

            i = ord(word)

            if direction == "right":
                ascii_value = ((i - base + shift) % 26) + base
            elif direction == "left":
                ascii_value = ((i - base - shift) % 26) + base
            else:
                return

            cipher += chr(ascii_value)
        elif word.isdigit():
            continue
        else:
            cipher += word




    with open(filename, "w") as out:
            out.write(cipher)
ceaser_cipher("text.txt",3,"left")