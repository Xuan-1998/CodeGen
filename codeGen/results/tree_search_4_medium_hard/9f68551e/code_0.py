def min_mana(monster_times, monster_healths):
    n = len(monster_times)
    dp = [[float('inf')] * (monster_times[-1] + 1) for _ in range(n + 1)]

    dp[0][0] = 0

    for i in range(1, n + 1):
        for t in range(monster_times[i - 1], monster_times[i] + 1):
            if t < monster_times[i - 1]:
                dp[i][t] = dp[i - 1][monster_times[i - 1]]
            elif t == monster_times[i - 1]:
                dp[i][t] = monster_healths[i - 1] + dp[i - 1][0]
            else:
                if t - monster_times[i - 1] < k_i:
                    dp[i][t] = dp[i - 1][k_i - i]
                elif t - monster_times[i - 1] == k_i:
                    dp[i][t] = h_i + dp[i - 1][0]
                else:
                    dp[i][t] = min(dp[i - 1][k_i - i] + h_i, 1 + dp[i - 1][t - k_i])

    return dp[n][0]
