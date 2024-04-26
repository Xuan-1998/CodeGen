def remove_duplicates(input_str):
    char_set = set()
    result_str = ""

    # Iterate through the input string
    for char in input_str:
        # Check if the character is not already in the set
        if char not in char_set:
            # Add the character to the set and append it to the result string
            char_set.add(char)
            result_str += char

    return result_str

# Read input from stdin
input_str = input()

# Print the result to stdout
print(remove_duplicates(input_str))
