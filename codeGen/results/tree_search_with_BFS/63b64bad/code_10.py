import sys
from collections import defaultdict

def dfs(i, a, dp, visited, cycle):
    visited[i] = True
    cycle[i] = True
    next_i = i + a[i] if i % 2 == 1 else i - a[i]
    if 2 <= next_i <= n:
        if cycle[next_i]:
            dp[i] = -1
        elif dp[next_i] == 0 and not visited[next_i]:
            dfs(next_i, a, dp, visited, cycle)
        if dp[next_i] != -1 and dp[i] != -1:
            dp[i] = dp[next_i] + a[i]
    else:
        dp[i] = a[i] if i % 2 == 1 else 0
    cycle[i] = False

n = int(sys.stdin.readline())
a = [0] + list(map(int, sys.stdin.readline().split()))
dp = [0]*(n+1)
visited = [False]*(n+1)
cycle = [False]*(n+1)

for i in range(2, n+1):
    if not visited[i]:
        dfs(i, a, dp, visited, cycle)

for i in range(2, n+1):
    print(dp[i] if dp[i] != -1 else -1)

