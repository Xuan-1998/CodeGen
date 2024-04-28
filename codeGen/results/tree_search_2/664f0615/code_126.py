def max_distance_speed_change(initial_speed, final_speed, time, speed_limit):
    dp = [0] * (time + 1)
    dp[0] = initial_speed

    for t in range(1, time + 1):
        if t == 1:
            dp[t] = min(final_speed, max(dp[t - 1] - speed_limit, initial_speed))
        else:
            dp[t] = min(final_speed, max(min(dp[t - 1]) - speed_limit, dp[0]))

    return sum(range(dp[i], dp[i - 1], -1)) if i > 0 else 0 for i in range(1, time + 1))

initial_speed = int(input())
final_speed = int(input())
time = int(input())
speed_limit = int(input())

print(max_distance_speed_change(initial_speed, final_speed, time, speed_limit))
