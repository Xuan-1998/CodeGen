def remove_duplicates(Str):
    char_dict = {}
    unique_str = ""
    i = 0
    j = 0
    
    for char in Str:
        if char not in char_dict:
            char_dict[char] = True
            unique_str += char
            j += 1
        else:
            i += 1
            
    return unique_str[i:]
