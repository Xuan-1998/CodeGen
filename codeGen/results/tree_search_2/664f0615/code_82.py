def max_path_length(initial_speed, final_speed, time_limit, max_change):
    dp = [[0] * (time_limit + 1) for _ in range(final_speed + 1)]

    for i in range(1, final_speed + 1):
        if i <= initial_speed:
            dp[i][1] = min(i * 100, time_limit)
        else:
            dp[i][1] = min(dp[initial_speed][0], time_limit)

        for t in range(2, time_limit + 1):
            if abs(i - initial_speed) > max_change:
                break
            dp[i][t] = dp[i][t-1]
            if i <= final_speed and abs(i - final_speed) <= max_change:
                dp[i][t] = min(dp[i][t], dp[final_speed][t-1])
    return dp[final_speed][time_limit]

initial_speed, final_speed, time_limit, max_change = [int(x) for x in input().split()]
print(max_path_length(initial_speed, final_speed, time_limit, max_change))
