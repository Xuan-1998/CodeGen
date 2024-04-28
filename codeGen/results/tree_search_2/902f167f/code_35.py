from sys import stdin

def min_squares(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i < j:
                continue
            min_squares = float('inf')
            for s in range(1, min(i, j) + 1):
                dp[i][j] = min(dp[i - s][j - s] + 1, min_squares)
            if i == j:
                dp[i][j] = 1

    return dp[n][m]

n, m = map(int, stdin.readline().split())
print(min_squares(n, m))
