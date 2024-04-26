def remove_duplicates(Str):
    char_set = set()
    result = []
    
    for char in Str:
        if char not in char_set:
            char_set.add(char)
            result.append(char)
            
    return "".join(result)

Str = input()
print(remove_duplicates(Str))
