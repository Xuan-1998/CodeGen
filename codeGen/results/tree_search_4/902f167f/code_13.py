import sys

def min_squares(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                dp[i][j] = 1
            elif i > 0 and j > 0:
                min_squares = sys.maxsize
                for k in range(1, min(i, j) + 1):
                    min_squares = min(min_squares, dp[max(0, i - k)][max(0, j - k)] + 1)
                dp[i][j] = min_squares

    return dp[n][m]

# Example usage:
n, m = map(int, input().split())
print(min_squares(n, m))
