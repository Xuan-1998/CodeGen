import sys

initial_speed, final_speed, time, allowed_change = [int(x) for x in input().split()]

dp = [[0] * (final_speed - initial_speed + 1) for _ in range(time+1)]

for i in range(1, time+1):
    for j in range(initial_speed, min(final_speed, i*initial_speed//time)+1):
        dp[i][j-initial_speed] = max(dp[i-1][j], (j+allowed_change-min(j, initial_speed)) if i > 1 else 0)

print(max([dp[i][j] for i in range(time+1) for j in range(initial_speed, final_speed+1)]))
