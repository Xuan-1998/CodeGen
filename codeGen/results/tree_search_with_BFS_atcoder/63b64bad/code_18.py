import sys
sys.setrecursionlimit(200005)

n = int(input().strip())
a = [0] + list(map(int, input().strip().split()))
dp = [-1] * (n+1)
visited = [0] * (n+1)

def dfs(i, y):
    if i <= 0 or i > n:
        return y
    if visited[i] == 1:
        return -1
    if dp[i] != -1:
        return dp[i] + y
    visited[i] = 1
    dp[i] = dfs(i + a[i], y + a[i])
    if dp[i] != -1:
        dp[i] -= y
    else:
        visited[i] = 0
    return dp[i]

for i in range(2, n+1):
    if dp[i] == -1:
        dfs(i, 0)
    print(dp[i])

