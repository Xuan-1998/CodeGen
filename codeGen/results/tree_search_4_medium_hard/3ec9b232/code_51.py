import sys
from collections import defaultdict

dp = defaultdict(int)
n, m = map(int, input().split())
for i in range(n):
    dp[m[i]] += 1
m.sort()
ans = 0
prev_m = -1
for i in range(n):
    if m[i] != prev_m:
        for k in range(i+1, n):
            ans += (dp[k-1] * (k-1-m[i-1])) % (10**9 + 7)
    prev_m = m[i]
print(ans % (10**9 + 7))
