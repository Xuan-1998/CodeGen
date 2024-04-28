code
import sys

initial_speed, final_speed, time, max_allowed_diff = [int(x) for x in input().split()]

dp = [[[0]*101] * 101]

for i in range(time):
    dp[i+1][final_speed] = max(dp[i][final_speed], dp[i][max(0, min(final_speed - initial_speed, max_allowed_diff))]) + abs(final_speed - initial_speed) / (i+2)

for i in range(time-1, 0, -1):
    dp[i][max(0, min(final_speed - initial_speed, max_allowed_diff))] = max(0, min(abs(final_speed - initial_speed), max_allowed_diff)) / (i+1)

print(max(dp[time][final_speed], dp[time][max(0, min(final_speed - initial_speed, max_allowed_diff))]))
