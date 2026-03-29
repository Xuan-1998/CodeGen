import sys

n, k = map(int, input().split())
s = input()

if k <= n:
    if s[n-1] < s[:k-1].min():
        result = s[:-1]
    else:
        result = s * 2
else:
    result = s

print(result)
