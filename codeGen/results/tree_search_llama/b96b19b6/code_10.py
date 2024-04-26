def remove_duplicates():
    Str = input()
    seen = set()
    result = ""
    
    for char in Str:
        if char not in seen:
            seen.add(char)
            result += char
    
    print(result)

remove_duplicates()
