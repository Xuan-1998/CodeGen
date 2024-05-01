from functools import lru_cache

@lru_cache(None)
def solve(m, N):
    dp = [[0] * (N + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        dp[i][0] = 1
        for j in range(1, N + 1):
            dp[i][j] = sum(dp[k][j - 1] for k in range(i)) + (dp[i - 1][j] if i > 0 else 0)

    return dp[m][N]

m, N = map(int, input().split())
print(solve(m, N) % (10**9 + 7))
