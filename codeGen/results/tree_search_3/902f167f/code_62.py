def min_squares(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                dp[i][j] = 1
            elif i * i <= j:
                min_val = float('inf')
                for k in range(1, i + 1):
                    if k * k <= j - (i - k) and dp[i - k][j - (i - k)] + 1 < min_val:
                        min_val = dp[i - k][j - (i - k)] + 1
                dp[i][j] = min_val
            else:
                dp[i][j] = dp[i][j - i]

    return dp[n][m]


n, m = map(int, input().split())
print(min_squares(n, m))
