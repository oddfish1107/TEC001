def keywordfinder(filename,keyword):
    lines = []
    try:
        with open(filename, "r", encoding='utf-8') as f:
            for line, number in enumerate(f, start=1):
                if keyword in number:
                    lines.append(line)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    return lines

print(keywordfinder("text.txt",'python'))