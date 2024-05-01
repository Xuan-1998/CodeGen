import collections

def build_suffix_tree(s):
    n = len(s)
    sigma = sorted(set(s))
    L = [0] * (n + 1)
    for i in range(n):
        L[i + 1] = L[i] + 1 if s[i] == sigma[0] else 0
    h = 0
    while 2 ** h <= n:
        h += 1
    for i in range(2 ** h, -1, -1):
        j = min(n, i)
        while L[j] > L[j - 1]:
            j -= 1
        if sigma[L[j]] == s[j]:
            sigma.remove(s[j])
            n -= 1
        else:
            break
    return collections.defaultdict(list)

def find_common_substrings(suffix_tree_str1, suffix_tree_str2):
    common_substrings = set()
    for node in suffix_tree_str1:
        if node in suffix_tree_str2:
            common_substrings.add(node)
    return list(common_substrings)

def count_non_overlapping_substrings(common_substrings):
    count = 0
    for i, substring in enumerate(common_substrings):
        for j in range(i + 1, len(common_substrings)):
            if common_substrings[j].startswith(substring) or common_substrings[j].endswith(substring):
                break
        else:
            count += 1
    return count

# Read input strings from stdin
str1 = input()
str2 = input()

# Create suffix trees for str1 and str2
suffix_tree_str1 = build_suffix_tree(str1)
suffix_tree_str2 = build_suffix_tree(str2)

# Find common substrings
common_substrings = find_common_substrings(suffix_tree_str1, suffix_tree_str2)

# Count non-overlapping substrings
max_common_substrings = count_non_overlapping_substrings(common_substrings)

# Print the answer to stdout
print(max_common_substrings)
