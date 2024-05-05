import sys

n, k = map(int, sys.stdin.readline().split())
s = sys.stdin.readline().strip()

if k <= n - 1:
    if len(s[:-1]) == k:
        print(s[:-1])
        sys.exit()
if k >= n:
    if len(s * (k // n + 1)) == k:
        print(s * (k // n + 1))
        sys.exit()

if len(s) < k:
    if k % 2 == 1:  
        print((s + s)[:k - 1] + s[-1])
    else: 
        print(s * (k // n))

print(min([s[:-1], s + s][:k])) if k <= n - 1 else min([s * (k // n), (s + s)[:k - 1] + s[-1]])
