import sys

# Read input
initial_speed, final_speed, time, max_diff = map(int, input().split())
speeds = list(range(initial_speed, final_speed+1))

dp = [[0] * (max_diff + 1) for _ in range(time + 1)]

for t in range(2, time + 1):
    for diff in range(max_diff + 1):
        dp[t][diff] = max(dp[t-1][min(diff+speeds[t-1]-initial_speed, max_diff)], 
                          dp[t-1][max(-diff-speeds[t-1]+final_speed, -max_diff)])
        
print(dp[time][max_diff])
