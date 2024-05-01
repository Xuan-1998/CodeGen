def min_tiles(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i <= 1 or j <= 1:
                dp[i][j] = 0
            else:
                min_tiles = float('inf')
                for k in range(min(i, j), 0, -1):
                    if i % k == 0 and j % k == 0:
                        min_tiles = min(min_tiles, dp[i // k][j // k] + (i // k) * (j // k))
                dp[i][j] = min_tiles

    return dp[n][m]

n, m = map(int, input().split())
print(min_tiles(n, m))
