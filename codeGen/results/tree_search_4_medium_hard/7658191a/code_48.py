def max_score(n, k, z, a):
    dp = [[0] * (k + 1) for _ in range(k + 1)]

    # Base case: after 0 moves and j moves to the left, the maximum score is 0
    for j in range(k + 1):
        dp[0][j] = 0

    # Fill in the rest of the table based on transitions
    for i in range(1, k + 1):
        for j in range(min(i, z) + 1):
            if j == 0:
                dp[i][j] = max(dp[i - 1][0], a[i])
            else:
                dp[i][j] = max(dp[i - 1][j - z] + a[i], dp[i - 1][j])

    return dp[k][0]
