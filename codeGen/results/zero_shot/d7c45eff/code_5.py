import sys

n, k = map(int, input().split())
s = input()

# Case 1: Deleting the last character
result = s[:k]

# Case 2: Duplicating the string
if k > n:
    result = s + s[:k-n]
else:
    result = s

print(result)
