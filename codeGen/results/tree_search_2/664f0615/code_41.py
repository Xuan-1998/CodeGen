def max_distance(initial_speed, final_speed, time, max_change):
    dp = [[0] * (time + 1) for _ in range(final_speed - initial_speed + 1)]
    
    for i in range(1, time + 1):
        for j in range(min(i - 1, final_speed - initial_speed), -1, -1):
            if abs(j - dp[j][i-1]) <= max_change:
                dp[j][i] = max(dp[j][i], dp[j][i-1] + j)
    
    return max(dp)

initial_speed, final_speed, time, max_change = [int(x) for x in input().split()]
print(max_distance(initial_speed, final_speed, time, max_change))
