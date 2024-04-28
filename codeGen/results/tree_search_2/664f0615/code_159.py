def max_length(initial_speed, final_speed, time, max_change):
    dp = [[0] * (final_speed + 1) for _ in range(time + 1)]
    
    for i in range(1, time + 1):
        prev_speed = initial_speed
        for j in range(min(initial_speed, final_speed), max(initial_speed, final_speed) + 1):
            if abs(j - prev_speed) <= max_change:
                dp[i][j] = dp[i-1][prev_speed] + (j * i)
            else:
                prev_speed = min(max(prev_speed, j), final_speed)
                dp[i][j] = dp[i-1][prev_speed] + (j * i)
        initial_speed = final_speed
    return max(dp[-1])

initial_speed, final_speed, time, max_change = map(int, input().split())
print(max_length(initial_speed, final_speed, time, max_change))
