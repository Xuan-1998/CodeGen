def remove_duplicates(Str):
    seen = set()
    result = ''
    for char in Str:
        if char not in seen:
            seen.add(char)
            result += char
    return result

input_str = input()
print(remove_duplicates(input_str))
