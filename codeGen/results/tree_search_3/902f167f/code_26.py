from math import sqrt

def min_squares(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 or j == 1:
                dp[i][j] = 1
            else:
                min_count = float('inf')
                for k in range(1, int(sqrt(i)) + 1):
                    if (i - k) * j >= k ** 2:
                        min_count = min(min_count, dp[k][j] + dp[i-k][j])
                for m in range(1, int(sqrt(j)) + 1):
                    if i * (j - m) >= m ** 2:
                        min_count = min(min_count, dp[i][m] + dp[i][j-m])
                dp[i][j] = min_count

    return dp[n][m]

n, m = map(int, input().split())
print(min_squares(n, m))
