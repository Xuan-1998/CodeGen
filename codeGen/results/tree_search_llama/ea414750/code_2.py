import sys

def find_overlapping_pairs(s):
    # Create a dictionary to store the starting indices of all occurrences of 'bear'
    bear_indices = {}
    for i in range(len(s) - 3):  # Iterate through the string, considering substrings of length 4 (since 'bear' has 4 characters)
        if s[i:i+4] == 'bear':
            bear_indices.setdefault(i, []).append(i)  # Add the current index to the list of indices for this occurrence

    overlapping_pairs = 0
    for i in range(len(s) - 3):  # Iterate through the string again, considering substrings of length 4
        if s[i:i+4] == 'bear':
            for j in bear_indices.get(i, []):
                overlapping_pairs += 1  # If we find a pair of indices that overlap with this occurrence, increment our count

    return overlapping_pairs

# Read the input string from stdin
s = sys.stdin.readline().strip()

# Calculate and print the number of overlapping pairs
print(find_overlapping_pairs(s))
