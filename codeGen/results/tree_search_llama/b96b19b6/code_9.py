def remove_duplicates(Str):
    # Sort the characters in the string
    sorted_str = sorted(list(Str))
    
    # Initialize an empty string to store the result
    result = ""
    
    # Iterate through the sorted string
    for char in sorted_str:
        # Check if the current character is not equal to the previous one
        if len(result) == 0 or char != result[-1]:
            # If it's not a duplicate, add it to the result string
            result += char
    
    return result

# Receive input from stdin
Str = input()

# Print the output to stdout
print(remove_duplicates(Str))
