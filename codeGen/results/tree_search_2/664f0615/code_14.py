from collections import namedtuple

SpeedDiff = namedtuple('SpeedDiff', 'speed diff')

def solve():
    initial_speed, final_speed, time, max_speed_diff = map(int, input().split())
    
    dp = [[0] * (max_speed_diff + 1) for _ in range(time + 1)]
    prev_speeds = [0] * (time + 1)
    
    for i in range(1, time + 1):
        for diff in range(max_speed_diff + 1):
            if i == 1:
                dp[i][diff] = min(initial_speed, final_speed - diff)
            elif prev_speeds[i - 1] + diff <= final_speed and diff <= max_speed_diff:
                dp[i][diff] = dp[i-1][diff] + (min(final_speed - diff, prev_speeds[i-1] + diff) if i < time else min(final_speed - diff, prev_speeds[-2] + diff))
            else:
                dp[i][diff] = dp[i-1][diff]
        
        prev_speeds[i] = max(0, dp[i].index(max(dp[i])) - 1)
    
    return sum((prev_speeds[i] - i) for i in range(time)) * (min(final_speed, initial_speed))

print(solve())
