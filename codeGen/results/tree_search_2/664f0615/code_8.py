def max_path_length(initial_speed, final_speed, time, max_speed_diff):
    dp = [[0] * (max_speed_diff + 1) for _ in range(time + 1)]
    dp[0][0] = initial_speed

    for i in range(1, time + 1):
        for diff in range(max_speed_diff + 1):
            if diff == 0:
                dp[i][diff] = dp[i-1][diff]
            elif i < time:
                for prev_diff in range(diff - 1, -1, -1):
                    if abs(dp[i-1][prev_diff] - (dp[i-1][prev_diff] + max_speed_diff)) <= max_speed_diff:
                        dp[i][diff] = min(dp[i-1][prev_diff], initial_speed + i * (final_speed - initial_speed) // time)
            else:
                dp[i][diff] = initial_speed

    return max(dp[-1])

initial_speed, final_speed, time, max_speed_diff = map(int, input().split())
print(max_path_length(initial_speed, final_speed, time, max_speed_diff))
