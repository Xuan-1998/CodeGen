import sys

# Read input from stdin
n = int(input())
s = input()
a = [int(x) for x in input().split()]

# Preprocess the input
freq = {}
for i, c in enumerate('abcdefghijklmnopqrstuvwxyz'):
    freq[c] = a[i]

ways = 0
max_len = 0
min_substrings = sys.maxsize

# Iterate over the string
count = 0
current_len = 0
for char in s:
    if freq[char] > 0:
        count += 1
        current_len += 1
        freq[char] -= 1
        if count == 26:
            ways += 1
            max_len = max(max_len, current_len)
            min_substrings = min(min_substrings, 1)
    else:
        count = 0
        current_len = 0

# Print the results
print(ways % (10**9 + 7))
print(max_len)
print(min_substrings)
