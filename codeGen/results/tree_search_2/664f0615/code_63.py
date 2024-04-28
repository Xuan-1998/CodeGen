from sys import stdin

initial_speed, final_speed = map(int, stdin.readline().split())
time, max_allowed_change = map(int, stdin.readline().split())

dp = [[0] * (time + 1) for _ in range(max_allowed_change + 1)]

for i in range(1, time + 1):
    dp[0][i] = i
    for j in range(min(initial_speed, final_speed), max(initial_speed, final_speed)):
        if j - initial_speed <= max_allowed_change:
            dp[j - initial_speed][i] = max(dp[j - initial_speed][i], dp[min(j - initial_speed, 0)][i - 1] + 1)

print(max(dp[-1]))
