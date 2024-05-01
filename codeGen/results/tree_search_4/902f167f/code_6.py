import sys

def min_tiles(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 or j == 1:
                dp[i][j] = 1
            else:
                min_tiles = float('inf')
                for k in range(1, min(i, j) + 1):
                    min_tiles = min(min_tiles, dp[max(0, i-k)][max(0, j-k)] + 1)
                dp[i][j] = min_tiles

    return dp[n][m]

n, m = map(int, sys.stdin.readline().split())
print(min_tiles(n, m))
