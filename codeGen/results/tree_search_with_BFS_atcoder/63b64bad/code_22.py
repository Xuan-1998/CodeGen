import sys

def solve():
    n = int(sys.stdin.readline())
    a = [0] + list(map(int, sys.stdin.readline().split()))
    dp = [0]*(n+1)
    visited = [0]*(n+1)
    cycle = [0]*(n+1)

    def dfs(x):
        visited[x] = 1
        y = a[x]
        nx = x + a[x]
        if nx > n or nx <= 0:
            dp[x] = y
        elif visited[nx] and not cycle[nx]:
            dp[x] = y + dp[nx]
        elif cycle[nx] or (visited[nx] and cycle[x]):
            dp[x] = -1
            cycle[x] = 1
        else:
            dp[x] = y + dfs(nx)
        visited[x] = 0
        return dp[x]

    for i in range(2, n+1):
        if not cycle[i]:
            dfs(i)

    for i in range(2, n+1):
        print(dp[i])

solve()

