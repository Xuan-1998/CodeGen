import sys
from collections import defaultdict

n, m, h = map(int, input().split())
s = list(map(int, input().split()))

p = [0] + s

ans = 1.0
for k in range(n-1, -1, -1):
    if sum(p[i] for i in range(h+1, m+1)) >= k:
        ans += (sum(1 for i in range(k+1) if p[i]) - sum(1 for i in range(k+h+1) if p[i])) / (k+1)
    else:
        break

print(ans or -1)
