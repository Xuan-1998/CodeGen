# Step 1: Read input
n = int(input())
s = input()
a = [int(x) for x in input().split()]

# Step 2: Initialize variables
num_ways = 0
max_len = 0
min_substrings = float('inf')

# Step 3: Iterate over the string and find the maximum length of each character
char_max_len = {}
for i, c in enumerate(s):
    if c not in char_max_len:
        char_max_len[c] = a[ord(c) - ord('a')]
    for j in range(i+1, min(i+char_max_len[c]+1, n)):
        if s[j] == c and (j-i+1 > max_len or (j-i+1 == max_len and i-j+1 < min_substrings)):
            max_len = j-i+1
            min_substrings = i-j+1
    for j in range(i-char_max_len[c]+1, -1, -1):
        if s[j] != c:
            break
        char_max_len[c] -= 1
    while i < n and s[i] == c:
        i += 1

# Step 4: Calculate the number of ways to split the string
for i in range(n):
    if i+1 >= max_len:
        num_ways = (num_ways + 1) % (10**9 + 7)
    for j in range(i+max_len, n):
        if s[i] == s[j]:
            char_max_len[s[i]] -= 1
        else:
            break

# Step 5: Print output
print(num_ways)
print(max_len)
print(min_substrings)
