import math

def min_tiles(n, m):
    dp = [[math.inf for _ in range(m+1)] for _ in range(n+1)]

    for j in range(m+1):
        dp[0][j] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            for k in range(1, math.isqrt(i) + 1):
                for l in range(1, math.isqrt(j) + 1):
                    dp[i][j] = min(dp[i][j], dp[i-k][j-l] + 1)

    return dp[n][m]

n, m = map(int, input().split())
print(min_tiles(n, m))
