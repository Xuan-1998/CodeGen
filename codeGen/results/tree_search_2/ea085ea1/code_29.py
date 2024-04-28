import sys
from collections import defaultdict

# Read the input strings
N = int(input())
str1 = input().strip()
str2 = input().strip()

trie = defaultdict(list)
max_length = 0

# Preprocess the input strings and store their substrings in a trie
for i in range(N):
    for j in range(i+1, N+1):
        substring = str1[i:j]
        if len(substring) > max_length:
            max_length = len(substring)
        trie[substring].append((i, j))

for i in range(N):
    for j in range(i+1, N+1):
        substring = str2[i:j]
        if len(substring) > max_length:
            max_length = len(substring)
        if substring in trie:
            for (start1, end1), (start2, end2) in zip(trie[substring], trie[substring]):
                if start2 >= start1 and end2 <= end1:
                    yield end1 - start1 + 1
