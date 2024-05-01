import sys

def find_common_substrings(str1, str2):
    # Create a suffix tree for each input string
    str1_tree = suffix_tree(str1)
    str2_tree = suffix_tree(str2)

    # Initialize variables to keep track of common substrings
    common_substrings = 0
    max_length = 0

    # Traverse the suffix trees and find common substrings
    for node in str1_tree.traverse():
        if node.value in str2_tree:
            # Check if the substring is non-overlapping
            if node.start >= max_length:
                common_substrings += 1
                max_length = node.start

    return common_substrings

def suffix_tree(s):
    # Implement a basic suffix tree algorithm here (e.g., Ukkonen's algorithm)
    pass

# Read input strings from stdin
str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()

# Find the maximum number of common non-overlapping substrings
common_substrings = find_common_substrings(str1, str2)

print(common_substrings)  # Print the result to stdout
