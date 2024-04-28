def solve(n, m, nums):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 1

    for j in range(m + 1):
        if j % m != 0:
            dp[0][j] = 0
        else:
            dp[0][j] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if nums[i - 1] <= j and (dp[i - 1][j] or dp[i - 1][j % m]):
                dp[i][j] = 1
            else:
                dp[i][j] = 0

    return 1 if dp[n][m] else 0
