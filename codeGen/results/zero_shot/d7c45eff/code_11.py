import sys

n, k = map(int, sys.stdin.readline().split())
s = sys.stdin.readline().strip()

if n < k:
    print(s[:k])
else:
    if s[-1] <= s[k-1]:
        print(s[:k])
    else:
        print(s + s[:k-n])
