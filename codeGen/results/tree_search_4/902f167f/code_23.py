import sys

def min_tiles(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                dp[i][j] = 1
            elif i > 1 and j > 1:
                min_tiles = float('inf')
                for k in range(1, min(i, j) + 1):
                    w = i - k
                    h = j - k
                    if w > 0 and h > 0:
                        min_tiles = min(min_tiles, dp[w][h] + 1)
                dp[i][j] = min_tiles
            elif i == 1:
                dp[i][j] = j
            elif j == 1:
                dp[i][j] = i

    return dp[n][m]

if __name__ == "__main__":
    n, m = map(int, input().split())
    print(min_tiles(n, m))
