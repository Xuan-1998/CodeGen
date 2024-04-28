def remove_duplicates(input_str):
    seen_chars = set()
    result = []

    for char in input_str:
        if char not in seen_chars:
            seen_chars.add(char)
            result.append(char)

    return ''.join(result)

input_str = input().strip()

print(remove_duplicates(input_str))
