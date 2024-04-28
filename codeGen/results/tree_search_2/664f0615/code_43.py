from sys import stdin

def max_distance():
    initial_speed, final_speed = map(int, stdin.readline().split())
    time, speed_diff = map(int, stdin.readline().split())

    dp = [0] * (time + 1)
    for i in range(1, time + 1):
        if i == 1:
            dp[i] = min(initial_speed, final_speed) * i
        else:
            for j in range(max(0, initial_speed - speed_diff), min(final_speed, initial_speed + speed_diff) + 1):
                dp[i] = max(dp[i], dp[i-1] + j)

    return dp[-1]

print(max_distance())
