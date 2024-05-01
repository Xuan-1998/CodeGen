import sys
from collections import defaultdict

def build_trie(str):
    root = defaultdict(dict)
    for char in str:
        node = root
        for c in char:
            if c not in node:
                node[c] = {}
            node = node[c]
    return root

def common_substrings(str1, str2):
    trie = build_trie(str1 + '#' + str2)  # Add a delimiter to differentiate strings
    max_length = 0
    count = 0
    for char in trie:
        if char != '#':
            node = trie[char]
            length = 0
            while len(node) > 0 and char not in {'#', ''}:
                length += 1
                node = node[char]
                char = ''
            max_length = max(max_length, length)
            count += 1
    return count

len_str1, str1 = input().split()
len_str2, str2 = input().split()

print(common_substrings(str1, str2))
