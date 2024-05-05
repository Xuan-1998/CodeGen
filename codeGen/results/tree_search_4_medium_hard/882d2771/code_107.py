def beautySum(t, l, r):
    mod = 10**9 + 7
    dp = [[0] * (r - l + 1) for _ in range(t + 1)]

    for i in range(2, t + 1):
        for j in range(l, r + 1):
            if i % 2 == 0:
                dp[i][j - l] = min((dp[(i - 1)][k] + 1) for k in range(j // 2, j + 1))
            else:
                dp[i][j - l] = min((dp[(i - 1)][k] + 1) for k in range(2, (j + 1) // 2 + 1))

    return sum(dp[i][r - l] * i for i in range(t)) % mod
