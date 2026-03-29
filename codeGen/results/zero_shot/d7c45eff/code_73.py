import sys

def min_string(n, k, s):
    if k == n:
        return s
    elif k < n:
        return s[:-1]
    else:
        return s * (k // n) + s[:k % n]

n, k = map(int, input().split())
s = input()

print(min_string(n, k, s))
