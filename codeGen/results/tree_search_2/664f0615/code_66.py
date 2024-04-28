import sys

initial_speed, final_speed = map(int, input().split())
time, max_change = map(int, input().split())

dp = [[0] * (time + 1) for _ in range(final_speed + 1)]

for s in range(initial_speed, final_speed):
    for t in range(time + 1):
        if t == 0:
            dp[s][t] = 0
        elif t == 1:
            dp[s][t] = 1
        else:
            max_length = 0
            for prev_s in range(max(0, s - max_change), min(final_speed + 1, s + max_change + 1)):
                max_length = max(max_length, dp[prev_s][t - 1])
            dp[s][t] = t + max_length

print(dp[final_speed][time])
