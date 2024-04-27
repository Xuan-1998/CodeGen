def remove_duplicates(Str):
    seen = {}
    result = []
    
    for i, char in enumerate(Str):
        if char not in seen:
            seen[char] = i
            result.append(char)
            
    return ''.join(result)

input_str = input()
print(remove_duplicates(input_str))
