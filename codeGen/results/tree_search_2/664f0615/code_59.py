import sys

def solve():
    init_speed, final_speed, time, max_allowed_change = [int(x) for x in input().split()]
    
    dp = [[0] * (time + 1) for _ in range(final_speed - init_speed + 1)]
    
    dp[0][0] = 0
    
    for speed_diff in range(1, final_speed - init_speed + 1):
        for time_sec in range(1, time + 1):
            if abs(speed_diff) <= max_allowed_change:
                dp[speed_diff][time_sec] = max(dp[speed_diff][time_sec-1], dp[speed_diff-1][time_sec-1] + (speed_diff > 0))
            else:
                dp[speed_diff][time_sec] = dp[speed_diff][time_sec-1]
    
    return dp[final_speed - init_speed][time]

print(solve())
