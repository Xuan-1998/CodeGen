dp = [[0] * (max_time + 1) for _ in range(max_speed + 1)]

for time in range(1, max_time + 1):
    for curr_speed in range(min_speed, max_speed + 1):
        if curr_speed == min_speed or abs(curr_speed - prev_speed) <= max_speed_diff:
            dp[curr_speed][time] = max(dp[curr_speed][time-1], dp[prev_speed][time-1] + (curr_speed - prev_speed))
        else:
            dp[curr_speed][time] = dp[curr_speed][time-1]
        prev_speed = curr_speed

print(max(dp[-1]))
