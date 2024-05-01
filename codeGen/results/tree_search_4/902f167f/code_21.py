import sys

def min_squares(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif i < j:
                dp[i][j] = min(dp[i][k] + (n - k) // (i - k) for k in range(1, i + 1))
            else:
                dp[i][j] = min(dp[k][m] + (n - k) // (j - k) for k in range(1, j + 1))

    return dp[n][m]

if __name__ == "__main__":
    n, m = map(int, input().split())
    print(min_squares(n, m))
