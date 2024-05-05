def max_earn(k, n, c, total_amount_to_spend):
    dp = [[0 for _ in range(total_amount_to_spend + 1)] for _ in range(k + 1)]

    for i in range(1, k + 1):
        for j in range(1, total_amount_to_spend + 1):
            if j >= c * i:
                dp[i][j] = max(dp[i - 1][j - c * i], 0) + c * i
            else:
                dp[i][j] = dp[i][j]

    return dp[k][total_amount_to_spend], sum(1 for _ in range(n) if total_amount_to_spend >= c), []

