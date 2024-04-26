def remove_duplicates(Str):
    seen = set()
    result = []
    
    for char in Str:
        if char not in seen:
            seen.add(char)
            result.append(char)
    
    return ''.join(result)

Str = input()
print(remove_duplicates(Str))
