def min_cost_after_trips():
    n = int(input())
    dp = [[float('inf')] * (n + 1) for _ in range(3)]
    dp[0][0] = 0

    for i in range(n):
        t_i = int(input())
        j = 0
        while j <= i:
            if j == 0:  # no tickets used yet
                dp[0][i - j + 1] = min(dp[0][i - j + 1], (t_i - j) * 20)
            elif j < 90:  # one-trip ticket can be used
                dp[1][i - j + 1] = min(dp[1][i - j + 1], dp[0][j] + (t_i - j) * 20)
            else:  # 90-minute ticket can be used
                dp[2][i - j + 1] = min(dp[2][i - j + 1], dp[1][j // 90 * 90] + (t_i - j) * 50)

    return [min(dp[i][n]) for i in range(3)]
