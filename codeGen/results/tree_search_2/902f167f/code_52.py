import sys

def min_squares(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1:
                dp[i][j] = 1
            elif j == 1:
                dp[i][j] = 1
            else:
                k = min(i, j)
                while k * k <= i * j:
                    k -= 1
                dp[i][j] = min(dp[i - 1][k], dp[k][j]) + (i > k and j > k)

    return dp[n][m]

n, m = map(int, input().split())
print(min_squares(n, m))
