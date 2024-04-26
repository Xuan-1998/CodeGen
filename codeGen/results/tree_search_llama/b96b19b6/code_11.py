def remove_duplicates(Str):
    freq_map = {}
    for char in Str:
        if char in freq_map:
            freq_map[char] += 1
        else:
            freq_map[char] = 1

    result = ''
    for char in Str:
        if freq_map[char] == 1:
            result += char
            del freq_map[char]

    return result

Str = input()
print(remove_duplicates(Str))
