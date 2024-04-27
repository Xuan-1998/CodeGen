def remove_duplicates(Str):
    seen = set()  # Initialize an empty set to store unique characters
    result = ""  # Initialize an empty string to store the result

    for char in Str:
        if char not in seen:  # Check if the character is already in the set
            seen.add(char)  # Add the character to the set (removes duplicates)
            result += char  # Append the unique character to the result string

    return result
