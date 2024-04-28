def max_path_length(initial_speed, final_speed, time, max_change):
    dp = [0] * (time + 1)
    dp[0] = initial_speed

    for i in range(1, time + 1):
        if i == 1:
            dp[i] = min(final_speed, initial_speed + max_change)
        else:
            dp[i] = max(dp[i-1] - max_change, final_speed)

    return dp[-1]

initial_speed, final_speed, time, max_change = map(int, input().split())
print(max_path_length(initial_speed, final_speed, time, max_change))
