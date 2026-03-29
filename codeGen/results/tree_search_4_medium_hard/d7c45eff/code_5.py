import sys

def solve(n, k):
    if k <= n:
        return s[:k]
    else:
        return s * (k // n) + s[:k % n]

n, k = map(int, input().split())
s = input()
print(solve(n, k))
