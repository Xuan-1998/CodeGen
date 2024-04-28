import sys

initial_speed, final_speed = map(int, input().split())
time_to_travel = int(input())

allowed_change_in_speed = int(input())

dp = [[0] * (allowed_change_in_speed + 1) for _ in range(time_to_travel + 1)]

for i in range(1, time_to_travel + 1):
    dp[i][0] = min(i, final_speed)
    for diff in range(1, allowed_change_in_speed + 1):
        if i > 1:
            dp[i][diff] = max(dp[i-1][max(0, diff-1)], min(time_to_travel - i + 1, final_speed - initial_speed))
        else:
            dp[i][diff] = min(i, final_speed)

print(max(dp[time_to_travel]))
