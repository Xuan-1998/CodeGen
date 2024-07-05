python
def dfs(i, a, dp, visited):
    if i <= 0 or i > n:
        return 0
    if dp[i] is not None:
        return dp[i]
    if visited[i]:
        return -1
    visited[i] = True
    result = dfs(i + a[i], a, dp, visited)
    visited[i] = False
    if result == -1:
        dp[i] = -1
    else:
        dp[i] = result + a[i]
    return dp[i]

n = int(input().strip())
a = [0] + list(map(int, input().strip().split()))
dp = [None] * (n+1)
visited = [False] * (n+1)

for i in range(2, n+1):
    print(dfs(i, a, dp, visited))

