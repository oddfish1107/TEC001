def hex_manual(color_code):
    if len(color_code) != 7 or not color_code.startswith("#"):
        return False
    
    valid_chars = "0123456789abcdefABCDEF"
    
    hex_part = color_code[1:]
    
    for char in hex_part:
        if char not in valid_chars:
            return False
            
    return True
print(hex_manual("#0000FF"))