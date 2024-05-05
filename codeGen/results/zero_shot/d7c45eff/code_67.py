import sys

n, k = map(int, input().split())
s = input()

if n <= k:
    # If the original string is shorter than or equal to k, delete the last character
    result = s[:-1]
else:
    # If the original string is longer than k, duplicate it and truncate if necessary
    duplicated_s = s * 2
    result = duplicated_s[:k]

print(result)
