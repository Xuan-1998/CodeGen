def max_path_length(initial_speed, final_speed, time, max_change):
    dp = [[0] * (time + 1) for _ in range(final_speed - initial_speed + 1)]

    for i in range(1, time + 1):
        for j in range(initial_speed, final_speed):
            if abs(j - initial_speed) <= max_change:
                dp[j - initial_speed][i] = max(dp[j - initial_speed][i-1], dp[j - initial_speed][i-1] + 1)
            else:
                dp[j - initial_speed][i] = dp[j - initial_speed][i-1]

    return max(dp[-1])

initial_speed, final_speed, time, max_change = map(int, input().split())
print(max_path_length(initial_speed, final_speed, time, max_change))
