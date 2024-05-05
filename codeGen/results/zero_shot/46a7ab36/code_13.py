def alien_language(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        if i % 2 == 0:
            dp[i][1] = n - 1
        else:
            dp[i][1] = 1

    for j in range(2, m + 1):
        for i in range(1, n + 1):
            if 2 * i > n:
                dp[i][j] = (n - 1) * dp[0][j - 1]
            else:
                dp[i][j] = dp[0][j - 1] + dp[i][j - 1]

    return pow(10, 8) + 7
