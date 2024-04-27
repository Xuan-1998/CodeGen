from collections import OrderedDict

def remove_duplicates(Str):
    result = []
    seen_chars = OrderedDict()

    for char in Str:
        if char not in seen_chars:
            seen_chars[char] = None
            result.append(char)

    return ''.join(result)

input_str = input()
print(remove_duplicates(input_str))
