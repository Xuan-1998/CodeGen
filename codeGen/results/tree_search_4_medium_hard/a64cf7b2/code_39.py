import sys

def solve(n, m, T):
    dp = [[0] * (T+1) for _ in range(n+1)]

    for i in range(1, n+1):
        dp[i][0] = 0

    for u, v, t in [list(map(int, input().split())) for _ in range(m)]:
        for j in range(T, t-1, -1):
            if dp[u][j-t]:
                dp[v][j] = max(dp[v][j], dp[u][j-t]+1)

    return dp[n][T]

n, m, T = map(int, input().split())
print(solve(n, m, T))
