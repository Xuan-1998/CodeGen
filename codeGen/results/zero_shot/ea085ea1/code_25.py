import sys

# Read input from stdin
str1 = input().strip()
str2 = input().strip()

# Preprocess strings by sorting characters
str1 = ''.join(sorted(str1))
str2 = ''.join(sorted(str2))

# Initialize set to store common substrings
common_substrings = set()

# Function to check if two strings are the same
def are_strings_equal(s1, s2):
    return s1 == s2

# Traverse suffix tree of str1 and find common substrings with str2
i = j = 0
while i < len(str1) and j < len(str2):
    k = l = 0
    while k < len(str1[i:]) and l < len(str2[j:]):
        if are_strings_equal(str1[i+k], str2[j+l]):
            common_substrings.add(str1[i+k:j+l+1])
            i += 1
            j += 1
            k = l = 0
        elif str1[i+k] < str2[j+l]:
            k += 1
        else:
            j += 1

# Print maximum number of non-overlapping substrings
print(len(common_substrings))
