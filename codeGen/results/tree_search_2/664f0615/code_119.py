import sys

dp = [[0] * (101) for _ in range(101)]

initial_speed, final_speed = map(int, input().split())
max_change = int(input())

for time in range(2, 101):
    dp[time][1] = initial_speed
    for speed in range(2, 100):
        if abs(dp[time-1][speed] - dp[time-1][speed-1]) <= max_change:
            dp[time][speed] = min(dp[time-1][speed], dp[time-1][speed-1]) + dp[time-1][speed]
    dp[100][final_speed] = sys.maxsize

max_distance = 0
for speed in range(1, 101):
    if abs(initial_speed - final_speed) <= max_change and dp[100][speed] > max_distance:
        max_distance = dp[100][speed]

print(max_distance)
