n = int(input().strip())
a = [0] + list(map(int, input().strip().split()))

dp = [-1]*(n+1)
visited = [False]*(n+1)

def dfs(i):
    if i <= 0 or i > n:
        return 0
    if visited[i]:
        return -1
    visited[i] = True
    dp[i] = dfs(i+a[i]) + a[i]
    if dp[i] < 0:
        dp[i] = -1
    visited[i] = False
    return dp[i]

for i in range(2, n+1):
    if dp[i] == -1:
        dfs(i)

for i in range(2, n+1):
    print(dp[i])

