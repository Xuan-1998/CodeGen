import sys

def solve():
    n, m, T = map(int, input().split())
    dp = [[0] * (T+1) for _ in range(n+1)]

    for _ in range(m):
        u, v, t = map(int, input().split())
        for j in range(min(T, t), 0, -1):
            dp[v][j] = max(dp[v][j], dp[u][j-t] + 1)

    k = dp[n][T]
    print(k)
    for i in range(n-1, -1, -1):
        if dp[i][T] == k:
            print(i+1)
            break

solve()
