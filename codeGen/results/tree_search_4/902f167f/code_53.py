import sys

def min_squares(n, m):
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                dp[i][j] = 0
            elif i == 1 or j == 1:
                dp[i][j] = 1
            else:
                min_val = float('inf')
                for k in range(1, min(i, j) + 1):
                    min_val = min(min_val, dp[i - k][j] + dp[i][j - k] + 1)
                dp[i][j] = min_val

    return dp[n][m]

if __name__ == "__main__":
    n, m = map(int, input().split())
    print(min_squares(n, m))
