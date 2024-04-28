def max_length_segment():
    initial_speed, final_speed, time, diff = map(int, input().split())
    
    dp = [[0] * (final_speed + 1) for _ in range(time + 1)]
    
    for i in range(1, time + 1):
        for speed in range(initial_speed, final_speed + 1):
            if i == 1:
                dp[i][speed] = min(speed, initial_speed) * time
            else:
                dp[i][speed] = max(dp[i - 1][max(0, speed - diff)], dp[i - 1][min(final_speed, speed + diff)]) + time
    
    return max(dp[-1])

print(max_length_segment())
