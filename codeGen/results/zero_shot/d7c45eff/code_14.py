import sys

n = int(input())
s = input()
k = int(input())

if k > n:
    result = s * (k // n) + s[:k % n]
else:
    if s[k-1] < s[-1]:
        result = s[:-1]
    else:
        result = s

print(result)
