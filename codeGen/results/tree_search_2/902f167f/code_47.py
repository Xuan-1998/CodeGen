import sys

def min_squares(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 or j == 1:
                # base case: single row or column
                dp[i][j] = min(i - 1, j - 1)
            else:
                # recursive case: split rectangle into smaller ones
                for k in range(1, int(i ** 0.5) + 1):
                    for l in range(1, int(j ** 0.5) + 1):
                        dp[i][j] = min(dp[i][j], dp[i - k][j - l] + 1)

    return dp[n][m]

n, m = map(int, sys.stdin.readline().split())
print(min_squares(n, m))
