from sys import stdin
max_speed, min_speed = map(int, stdin.readline().split())
time, max_change = map(int, stdin.readline().split())

dp = [[0] * (min_speed + 1) for _ in range(time + 1)]

for i in range(1, time + 1):
    for j in range(max(min_speed, min_speed - max_change), min_speed + 1):
        dp[i][j] = dp[i-1][j-1] + (j * 1) if j <= min_speed else dp[i-1][max_speed] + (min_speed * 1)
    for j in range(max(min_speed, min_speed + max_change), min_speed + 2):
        dp[i][j] = dp[i-1][j-1] - (j * 1) if j >= min_speed else dp[i-1][min_speed] - (min_speed * 1)

print(max(dp[-1]))
