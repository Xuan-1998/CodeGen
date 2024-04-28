def max_length_path_segment():
    initial_speed, final_speed, time, allowed_change_in_speed = map(int, input().split())
    
    dp = [[0] * (allowed_change_in_speed + 1) for _ in range(time + 1)]
    
    for i in range(1, time + 1):
        for diff in range(abs(final_speed - initial_speed), allowed_change_in_speed + 1):
            if i == 1:
                dp[i][diff] = 0
            else:
                for j in range(min(initial_speed, final_speed) - 1, max(initial_speed, final_speed) + 2):
                    dp[i][diff] = max(dp[i][diff], dp[i-1][j-init_speed+j-final_speed] + abs(j-init_speed))
    
    return dp[time][allowed_change_in_speed]

print(max_length_path_segment())
