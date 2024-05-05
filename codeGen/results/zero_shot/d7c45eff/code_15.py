import sys

n, k = map(int, input().split())
s = input()

result = s[:k]

if len(s) > k and s[k-1] <= s[-1]:
    result = s[:-1]

print(result)
