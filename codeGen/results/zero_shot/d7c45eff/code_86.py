import sys

def solve(n, k):
    s = sys.stdin.readline().strip()
    if k > n:
        return s * (k // n) + (s[:k % n] if k % n != 0 else '')
    elif k == n:
        return s
    elif k < n:
        return s[:-1] if k < n - 1 else s

n, k = map(int, sys.stdin.readline().split())
print(solve(n, k))
