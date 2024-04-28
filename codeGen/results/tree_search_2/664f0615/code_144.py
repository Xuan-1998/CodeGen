from sys import stdin

initial_speed, final_speed = map(int, stdin.readline().split())
time, max_change_in_speed = map(int, stdin.readline().split())

dp = [[0] * (max_time + 1) for _ in range(final_speed - initial_speed + 1)]
for speed_diff in range(final_speed - initial_speed + 1):
    for time_taken in range(time + 1):
        if time_taken == 0:
            dp[speed_diff][time_taken] = 0
        elif time_taken == 1:
            dp[speed_diff][time_taken] = max(0, speed_diff) * (speed_diff <= max_change_in_speed)
        else:
            dp[speed_diff][time_taken] = max(dp[speed_diff][time_taken - 1], dp[min(final_speed - initial_speed, speed_diff + max_change_in_speed)][time_taken - 2]) + speed_diff

print(max(dp[-1]))
