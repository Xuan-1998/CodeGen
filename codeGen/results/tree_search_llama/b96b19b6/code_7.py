def remove_duplicates(Str):
    # Create an empty dictionary to store unique characters
    char_dict = {}
    
    # Iterate through each character in the input string
    for i, char in enumerate(Str):
        # Check if the character is not already in the dictionary
        if char not in char_dict:
            # If it's not, add it to the dictionary with its original index
            char_dict[char] = i
    
    # Convert the dictionary values (indices) back into a list and sort them
    sorted_indices = sorted(char_dict.values())
    
    # Use the sorted indices to retrieve the unique characters in their original order
    result_str = [Str[i] for i in sorted_indices]
    
    # Join the result string and return it
    return ''.join(result_str)

# Receive input from stdin
Str = input()

# Print the output to stdout
print(remove_duplicates(Str))
