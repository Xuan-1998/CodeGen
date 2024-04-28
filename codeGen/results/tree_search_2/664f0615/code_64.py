import sys

initial_speed, final_speed = map(int, input().split())
time, max_allowed_change = map(int, input().split())

dp = [[0] * (time + 1) for _ in range(max_allowed_change * time + 1)]

for i in range(1, max_allowed_change * time + 1):
    speed_diff = min(final_speed - initial_speed, i)
    for j in range(1, time + 1):
        if speed_diff <= max_allowed_change:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            break

print(max([dp[i][time] for i in range(max_allowed_change * time + 1) if dp[i][time]]))
