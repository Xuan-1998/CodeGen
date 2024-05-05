import sys
from collections import defaultdict

dp = [[0] * (int(1e6) + 1) for _ in range(int(1e6) + 1)]
max_val = max(a)

for i in range(max_val, -1, -1):
    for j in range(i, 0, -1):
        if a[i] % j == 0:
            dp[i][j] = (dp[i-1][j] or 1) if i > 0 else 1

res = sum(dp[i][j] for i in range(n+1) for j in range(1, max_val+1))
print(res % (10**9 + 7))
