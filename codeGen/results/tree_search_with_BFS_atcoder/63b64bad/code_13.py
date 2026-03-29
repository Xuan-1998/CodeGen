import sys
from collections import defaultdict

def dfs(x, val):
    if visited[x]:
        if not calculated[x]:
            dp[x] = -1
        return dp[x]
    visited[x] = True
    dp[x] = val + a[x]
    if x - a[x] > 0:
        dp[x] = max(dp[x], dfs(x - a[x], dp[x]))
    if x + a[x] <= n:
        dp[x] = max(dp[x], dfs(x + a[x], dp[x]))
    calculated[x] = True
    return dp[x]

n = int(sys.stdin.readline())
a = [0] + list(map(int, sys.stdin.readline().split()))

dp = defaultdict(int)
visited = [False] * (n + 1)
calculated = [False] * (n + 1)

for i in range(1, n + 1):
    if not visited[i]:
        dfs(i, 0)

for i in range(1, n + 1):
    print(dp[i] if dp[i] != -1 else -1)

