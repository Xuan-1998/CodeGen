def remove_duplicates(Str):
    seen = {}
    result = ""
    for char in Str:
        if char not in seen:
            seen[char] = 1
            result += char
    return result

# Receive input from stdin
Str = input()

# Print the answer to stdout
print(remove_duplicates(Str))
