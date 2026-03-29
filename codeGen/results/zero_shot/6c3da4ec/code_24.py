import sys
from itertools import combinations

n = int(input())
s = input()

max_or = 0
for i in range(1, n):
    for j in range(i+1, n):
        left, right = s[:i], s[i:]
        left_or, right_or = int(left, 2), int(right, 2)
        or_value = left_or | right_or
        max_or = max(max_or, or_value)

print(bin(max_or)[2:])
