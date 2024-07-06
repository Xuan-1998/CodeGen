import sys

n, k = map(int, sys.stdin.readline().split())
s = sys.stdin.readline().strip()

if k <= n:
    if k == 1:
        print(s[-1])
    else:
        print(s[:k])
else:
    if len(s) % 2 == 0 and k % 2 == 0:
        print(s * (k // len(s)))
    elif k % 2 == 1:
        print(s + s[:k-1])
    else:
        print(s + s[:-1])
