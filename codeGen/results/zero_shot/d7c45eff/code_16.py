import sys

n, k = map(int, sys.stdin.readline().split())
s = sys.stdin.readline().strip()

if k > n:
    print(s)
else:
    if k == n or s[k-1] <= s[0]:
        print(s[:k])
    else:
        print(s)
