code
max_diff = int(input())  # read maximum allowed change in speed from stdin
init_speed, final_speed = map(int, input().split())  # read initial and final speed from stdin
t = int(input())  # read time it takes to travel the distance from stdin

memo = {(diff, time): None for diff in range(max_diff + 1) for time in range(t + 1)}

dp = [[0] * (max_diff + 1) for _ in range(t + 1)]

for time in range(1, t + 1):
    for diff in range(max_diff + 1):
        if time == 1:
            dp[time][diff] = init_speed - diff
        elif time < t:
            dp[time][diff] = max(dp[time - 1][min(diff, abs(final_speed - init_speed) + 1)], dp[time - 1][max(-diff, abs(final_speed - init_speed) - 1)])
        else:  # time == t
            dp[time][diff] = min(final_speed, init_speed - diff)

print(max(dp[t]))
