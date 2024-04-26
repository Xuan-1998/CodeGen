import sys
from collections import OrderedDict

def circular_sequence(s):
    # Build the suffix tree
    suffixes = [s[i:] for i in range(len(s))]
    suffix_tree = OrderedDict()
    for suffix in suffixes:
        for char in suffix:
            if char not in suffix_tree:
                suffix_tree[char] = []
            suffix_tree[char].append(suffix)

    # Find repeated patterns using KMP
    def kmp(pattern, text):
        lps = [0] * (len(pattern) + 1)
        j = 0
        for i in range(1, len(text)):
            if text[i] == pattern[j]:
                j += 1
            if j == len(pattern):
                return True
            elif i < len(text) and text[i] != pattern[j]:
                j = lps[j]
        return False

    # Iterate over the suffix tree to find repeated patterns
    for char, suffixes in suffix_tree.items():
        for suffix in suffixes:
            if kmp(suffix, s):
                return "Circular"

    return "Not Circular"

# Read input from stdin
s = sys.stdin.readline().strip()

# Print output to stdout
print(circular_sequence(s))
