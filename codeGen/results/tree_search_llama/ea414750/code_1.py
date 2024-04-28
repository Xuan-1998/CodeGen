import re

def count_bear_pairs(input_string):
    # Find all occurrences of 'bear' in the input string using regular expression
    bear_indices = {m.start(): m.end() for m in re.finditer('bear', input_string)}

    # Initialize counter for overlapping pairs
    overlapping_pairs = 0

    # Iterate through the dictionary keys (start indices) to find overlapping pairs
    for i, j in zip(bear_indices.keys(), bear_indices.keys()[1:]):
        if j - i == 4:  # 'bear' has a length of 4 characters
            overlapping_pairs += 1

    return overlapping_pairs

# Read the input string from stdin
input_string = input().strip()

# Call the function to count the number of overlapping pairs
count = count_bear_pairs(input_string)

# Print the result to stdout
print(count)
