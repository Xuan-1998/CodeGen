import sys
from itertools import combinations

n = int(input())
s = input()

max_or_value = 0

# Generate all possible pairs of substrings
pairs = list(combinations(range(n), 2))

for pair in pairs:
    sub1, sub2 = s[:pair[0]], s[pair[0]+1:pair[1]]
    sub3, sub4 = s[:pair[1]], s[pair[1]+1:]
    
    # Calculate the bitwise OR of each pair
    or_value1 = int(sub1, 2) | int(sub2, 2)
    or_value2 = int(sub3, 2) | int(sub4, 2)

    # Update max_or_value if necessary
    max_or_value = max(max_or_value, or_value1, or_value2)

print(bin(max_or_value)[2:].zfill(n).lstrip('0') or '0')
