def max_path_length(initial_speed, final_speed, max_time, max_change):
    dp = [[[0 for _ in range(max_time + 1)] for _ in range(final_speed + 1)] for _ in range(final_speed + 1)]
    
    for time in range(1, max_time + 1):
        if time == 1:
            for speed in range(initial_speed, final_speed + 1):
                dp[speed][speed][time] = (final_speed - initial_speed) * 100
        else:
            for i in range(initial_speed, final_speed + 1):
                for j in range(max(final_speed - max_change, i), min(final_speed + max_change, j)):
                    if abs(j - i) <= max_change and dp[i][j][time - 1] > 0:
                        dp[j][j][time] = max(dp[j][j][time], dp[i][j][time - 1] + (j * 100))
    
    return max([dp[s][s][max_time] for s in range(initial_speed, final_speed + 1)])
