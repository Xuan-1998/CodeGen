def max_distance(initial_speed, final_speed, time, max_change):
    dp = [[0] * (final_speed + 1) for _ in range(time + 1)]

    for i in range(1, time + 1):
        for j in range(min(final_speed, initial_speed), -1, -1):
            if abs(j - initial_speed) <= max_change:
                dp[i][j] = min(dp[i-1][j], dp[i-1][initial_speed] + (j-initial_speed))
            else:
                dp[i][j] = dp[i-1][j]

    return dp[-1][-1]
