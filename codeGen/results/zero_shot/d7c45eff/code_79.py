import sys

n, k = map(int, input().split())
s = input()

if n <= k:
    # Duplicate the string until it reaches a length of k
    result = s * (k // len(s)) + s[:k % len(s)]
else:
    # Delete characters from the end of the string until it reaches a length of k
    result = s[:k]

print(result)
