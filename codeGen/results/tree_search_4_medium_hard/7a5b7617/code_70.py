import sys

def steady_tables(n, m):
    MOD = 1e9 + 7
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for j in range(m + 1):
        dp[0][j] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if j <= i:
                dp[i][j] = (dp[i - 1][j - 1] + sum(dp[k][j - 1] for k in range(i))) % MOD
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][m]

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    print(steady_tables(n, m))
