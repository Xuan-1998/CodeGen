from collections import defaultdict

def solve(str1, str2):
    # Preprocess the strings to create a suffix tree
    suffix_tree_str1 = {}
    for i in range(len(str1)):
        for j in range(i+1):
            suffix = str1[j:i+1]
            if len(suffix) == 0:
                continue
            if suffix not in suffix_tree_str1:
                suffix_tree_str1[suffix] = []
            suffix_tree_str1[suffix].append((j, i))

    suffix_tree_str2 = {}
    for i in range(len(str2)):
        for j in range(i+1):
            suffix = str2[j:i+1]
            if len(suffix) == 0:
                continue
            if suffix not in suffix_tree_str2:
                suffix_tree_str2[suffix] = []
            suffix_tree_str2[suffix].append((j, i))

    # Find the maximum number of common non-overlapping substrings between the two strings
    max_common_substrings = 0
    for suffix1 in suffix_tree_str1:
        if suffix1 not in suffix_tree_str2:
            continue
        common_substrings = 0
        for node1 in suffix_tree_str1[suffix1]:
            for node2 in suffix_tree_str2[suffix1]:
                if node1[0] >= node2[0] and node1[1] <= node2[1]:
                    common_substrings += 1
        max_common_substrings = max(max_common_substrings, common_substrings)

    return max_common_substrings

# Read the input from stdin
str1 = input().strip()
str2 = input().strip()

# Solve the problem and print the answer to stdout
print(solve(str1, str2))
