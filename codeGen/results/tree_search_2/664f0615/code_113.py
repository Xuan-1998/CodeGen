import sys

initial_speed, final_speed = map(int, input().split())
time, max_change = map(int, input().split())

dp = [[0] * (max_change + 1) for _ in range(time + 1)]

for t in range(1, time + 1):
    for d in range(max_change + 1):
        if t == 1:
            dp[t][d] = min(final_speed, initial_speed)
        elif d > 0 and abs(dp[t-1][d-1] - dp[t-1][d]) <= max_change:
            dp[t][d] = dp[t-1][d-1] + (dp[t-1][d-1] - dp[t-2][d-1])
        else:
            dp[t][d] = 0

print(max(dp[-1]))
