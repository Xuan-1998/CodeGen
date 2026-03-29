import sys

n = int(input())
s = input()

# Calculate the bitwise OR of each prefix with itself
prefix_or = [0] * (n + 1)
for i in range(n):
    prefix_or[i + 1] = prefix_or[i] ^ ord(s[i])

max_or = [0, 0]
current_or = 0

# Find the maximum possible value
for i in range(1, n - 1):
    if prefix_or[i] > current_or:
        current_or = prefix_or[i]
    elif prefix_or[n - 1 - i] > current_or:
        current_or = prefix_or[n - 1 - i]

max_or = [current_or, current_or]

# Calculate the bitwise OR of the two substrings
for i in range(1, n):
    if s[:i].count('0') == i and s[i:].count('1') == n - i:
        max_or[0] ^= int(s[:i], 2)
        max_or[1] ^= int(s[i:], 2)

print(bin(max_or[0] | max_or[1]).lstrip('0').lstrip(' '))
