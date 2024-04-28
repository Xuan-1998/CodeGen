import sys

min_speed, max_speed, time, max_speed_change = map(int, input().split())

dp = [[0] * (max_speed + 1) for _ in range(time + 1)]

for i in range(1, time + 1):
    for j in range(min_speed, max_speed + 1):
        dp[i][j] = dp[i-1][k] + 1 if abs(j-k) <= max_speed_change else 0
        k = min(max_speed, j - max_speed_change)
        while k >= min_speed and dp[i-1][k] < dp[i-1][max_speed]:
            k -= 1

print(dp[time][max_speed])
