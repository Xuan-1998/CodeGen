def min_squares(n, m):
    max_size = max(n, m)
    dp = [[float('inf')] * (max_size + 1) for _ in range(max_size + 1)]

    for i in range(max_size + 1):
        dp[i][0] = dp[0][i] = 1

    for size in range(1, max_size + 1):
        for i in range(size, max_size + 1):
            for j in range(size, max_size + 1):
                k = int((i ** 0.5) + 0.5)
                while k * k < i or k * k < j:
                    k += 1
                dp[i][j] = min(dp[i][j], dp[k - 1][k - 1] + (i - k * k) // k + (j - k * k) // k)

    return dp[n][m]

n, m = map(int, input().split())
print(min_squares(n, m))
