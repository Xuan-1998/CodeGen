def remove_duplicates(Str):
    unique_chars = set()
    result_str = ""
    
    for char in Str:
        if char not in unique_chars:
            unique_chars.add(char)
            result_str += char
    
    return result_str

Str = input().strip()
print(remove_duplicates(Str))
