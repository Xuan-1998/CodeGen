import sys
from itertools import combinations

n = int(input())
s = input()

# Generate all possible pairs of substrings
pairs = list(combinations(range(n), 2))

max_or_value = 0

for pair in pairs:
    start1, end1 = pair[0], pair[1]
    start2, end2 = pair[1], pair[2]

    # Calculate the bitwise OR of the integer values of the two substrings
    or_value = int(s[start1:end1+1], 2) | int(s[start2:end2+1], 2)

    max_or_value = max(max_or_value, or_value)

print(format(max_or_value, 'b').lstrip('0'))
