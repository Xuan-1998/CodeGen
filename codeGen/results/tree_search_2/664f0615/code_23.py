from sys import stdin

input()
init_speed, final_speed = map(int, stdin.readline().split())
time, max_speed_change = map(int, stdin.readline().split())

dp = [[0] * (final_speed + 1) for _ in range(time + 1)]

for i in range(1, time + 1):
    for speed in range(1, final_speed + 1):
        if speed <= init_speed:
            dp[i][speed] = 1
        elif speed == final_speed:
            dp[i][speed] = 1
        else:
            dp[i][speed] = max(dp[i-1][speed], dp[i-1][max(0, speed - max_speed_change)] + 1)

print(max(dp[-1]))
