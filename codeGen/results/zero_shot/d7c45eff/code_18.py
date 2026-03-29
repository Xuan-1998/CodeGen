import sys

n, k = map(int, input().split())
s = input()

if k >= n:
    result = s * (k // n)
    if k % n != 0:
        result += s[:k % n]
else:
    if k <= len(s):
        result = s[:-1] * (k - len(s))
    else:
        result = s + s[:k - len(s)]

print(result)
