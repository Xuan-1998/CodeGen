def unique_characters(Str):
    Str = list(Str)
    char_set = set()
    result = ''
    for char in Str:
        if char not in char_set:
            char_set.add(char)
            result += char
    return result

Str = input()
print(unique_characters(Str))
